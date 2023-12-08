---
title: Rollerball Debrief
publishDate: '2023-12-08T17:00:00+05:30'
categories: 
- Programming
tags:
- Programming
slug: rollerball-debrief
---

Since the semester is finally over, I think this is a good time to discuss my 
primary programming project over the last semester. This is unique enough to 
merit it's own blog post: It's something that impacted a lot of people at
scale, and also something I believe is novel and required a metric ton of
effort from my end to make a reality.

This is Rollerball, the COL333 competitive assignment for this semester. 

## Context

COL333 is a junior undergraduate/graduate bridge course in Artificial 
Intelligence, and one of the most valuable/fun courses undergrads do in their 
time. Multiple reasons why, primarily how _cool_ the field is right now, the 
competitive assignments, and the joy of seeing algorithms you create do tasks 
better than you could.

As TAs, we had to make two quizzes, work on one assignment and help grade the 
midterm and endterm. Seems simple enough. However, this time I wanted to 
do something special. The competitive assignment for every COL333 course is 
very exciting for students. In my opinion, the last offering's assignment was 
too simple, and basically ripped off an existing assignment with minor 
modifications and presented it to students.

I wanted to do something different. Something groundbreaking. Something that 
highlighted how IITD is on par with top universities when it comes to teaching,
and how we are capable of rolling out our own assignments from scratch.

Enter Rollerball. An obscure chess variant I dug up during the free time at 
my internship, Rollerball seemed like the perfect fit. No bots or strategy 
guides existed for it. The only working implementation existed in [Jocly][1], 
which used a generalized MCTS written in JS, so it was also near impossible to 
ape. It was venturing into the unknown, and exactly the kind of assignment 
bright minds would need to stay occupied. I quickly hacked up a working 
implementation in under a couple of weeks, and presented it the first time we 
had a TA meet.

There were supposed to be 5 assignments, and the second and fifth ones were 
competitive ones. The second assignment was a 4-mark warmup, while the 
last would be a 12-mark tournament. With the timeline set and consensus on what 
we should work on, I set out to wrap up the initial starter code.

## Rollerball v1

The amount of engineering that went into developing this probably places it in 
my top 3 projects of all time. And I've done a lot of projects. Rollerball 
shaped up to be one of those assignments where the student code is smaller 
than the TA code, and for good reason.

To keep things modular, I started out by separating the engine and the UI, 
since we don't need the UI while evaluating. The UI was then written in
JavaScript and Vue, because [chessboard.js][2] is a very nice javascript
chessboard library. This would then communicate with the client engine via 
WebSockets. I cooked up a small protocol based on [UCI][3], and things were 
good to go. We had made the entire car, but we didn't have an engine.

Deciding which language to code the engine in was tricky. Python was my first 
pick, because of how simple it is. WebSockets would also be well supported. 
However, the last offering's assignment was in Python, and instead of
developing a good algorithm, I went into optimization hell trying to create a
bitboard for Connect 4. Python is a terrible language for programming a fast
tree-search algorithm, and I didn't want students to even consider that path.

Which meant the engine was going to be written in C++. 

The first task was finding and creating a WebSocket library to communicate with 
the frontend. I settled on using websocketpp, which in turn used asio. These 
libraries were include-only, which meant students would be able to use a simple 
Makefile and wouldn't have to get their hands dirty with CMake or other build 
systems. I had a small C++ client up and running, which communicated with the 
frontend.

The next step was to create the move generation and validation algorithms. This 
was the core of the engine. My personal requirements were speed and robustness.
If you've done any chess programming, the standard board representation is 
via Bitboards, and the fastest way to generate moves is using Magic Bitboards
and sliding piece attacks.

There was just one gripe: This was _rollerball_, not chess. Chess doesn't have 
a gaping hole in the middle of the board. Chess doesn't have pieces bouncing off 
the corners. Chess doesn't have pieces whose direction of movement changes 
depending on their location. These issues threw any and all chess-specific
programming out the window, and I was back to square one on deciding how to
generate moves.

The first thing to notice was the four-fold symmetry. I mapped the squares on 
the board to integers, and created rotation maps: maps that would take one 
square to another when the board was rotated by 90 degrees. All I had to do now 
was generate moves for one quadrant, which was 10 squares. For a piece that 
didn't lie in these ten squares, I'd apply the transformation on the board 
to get that piece into these ten squares, generate the moves in this transformed 
coordinate space, and then map the squares back using the inverse transform.

![move generation](/articles/2023/res/movegen.png)

Note that there were 12 pieces, and 6 of them (the black ones) would seldom
be in the first 10 squares. Rotation was also an expensive operation. Instead 
of rotating, the faster technique was to maintain four boards, each of which 
would contain a particular rotation (0, 90, 180, 270). Also maintain four area
maps, which would map squares to which segment of the board they lay in, and
which board should be used to generate their moves.

Now that move generation was a bit simplified, it was time to think of move 
representation. Skylake has 64 kB L1 cache per core, which is a lot. Ideally,
the entire board should fit in a fraction of that space. Since this board was 
7x7, I represented each coordinate with 3 bits. A position then took 8 bits,
and a move took 16. The board would then contain piece positions (12 bytes),
and four boards (for preventing range errors, I let the boards be 8x8 for now).
The boards took 4x64 = 256 bytes each. This was encapsulated in a `BoardData` 
struct rather than the base `Board` struct. The `BoardData` struct now looked 
something like this:

```c++
struct BoardData {

    U8 w_rook_ws = pos(2,1);
    U8 w_rook_bs = pos(2,2);
    ...
    U8 b_pawn_ws = pos(4,5);
    U8 b_pawn_bs = pos(4,6);

    U8 board_0[64], board_90[64], board_180[64], board_270[64];
}
```

The board squares also had a representation of their own: two bits were reserved 
for color (white|black), and six bits for piece type. The piece type and color 
were one-hot encoded, so that you could use bitmasks to get and modify the type
and color quickly.

We now had a very small board, and a way to generate moves. The actual move 
generation logic that I initially wrote was super messy. For the bishop, it 
was an if-else over the ten squares, and I manually pushed moves onto a stack
depending on the case (This raised problems later). Checking for collisions 
for sliding pieces was also done manually, the brute-force way. Checking for 
reflections was also done via conditions. 

The next step was move validation. This involved checking if the king was in 
check, and if it was, restricting the set of possible moves. The initial 
version bruteforced this: it would basically evaluate the tree upto one move 
(2 ply), checking each of the possible moves, and seeing if the king was under 
threat as a result of any of them. If it was, it would simply discard the 
original move that put it under check.

```c++
bool Board::under_threat(U8 piece_pos) const {
    auto pseudolegal_moves = this->get_pseudolegal_moves_for_side(
            this->data.player_to_play ^ (WHITE | BLACK)
        );
    for (auto move : pseudolegal_moves) {
        if (getp1(move) == piece_pos) {
            return true;
        }
    }
    return false;
}
```

All this to get a simple assignment out the door. And we weren't done yet. The 
guidelines mentioned that people would be able to submit their assignments in 
C++, Python or Java. After dropping Java submissions because it was impossible 
to port the code to Java, we started working on a set of Python bindings. 
`pybind3` was our tool of choice, and the bindings it generated were quite 
usable. We also issued an advisory that students submitting in python may face 
issues because python is inherently slower, so they are strongly advised to 
code in c++.

Finally, the small things remained. Note that there was no move validation or
arbitration on the frontend, so how would the engine know that there was a
checkmate? This was done via move validation before sending the move to the
engine. Since the engine could not mutate the board passed to it, we would take
the gold board and check if the move the engine returned was in the set of
valid moves here. This was baked into the client. Another issue was timing: 
We had decided on giving a fixed 2 seconds per move, and there was ambiguity 
regarding what action to take if a user didn't return a move in the fixed 
duration, or if the user didn't return a valid move. These were fixed by 
consensus.

After this, I started working on the document. ChatGPT is great at TikZ, and 
after some prompting attempts, I had a cool-looking rollerball board in pure 
LaTeX (which is what was used to generate the diagram above :)) 

### Other requests

There was a decision between having a fixed time limit per move, or giving each 
engine a time budget (as is done in chess). Previous iterations of the course 
had done the latter, while we believed doing and implementing the former was 
easier, as students would crib about their clock going out of sync with the 
clock on the arbiter. We would need to modify the protocol to sync the arbiter 
clock with the student clock at each move, and that would take time, which we 
didn't have.

Other issues centered around keeping the board size flexible, as was done in 
all of the previous iterations of the prof's course. I felt like this was more 
of a non-issue, as the final assignment would be competitive and centered
around Deep Learning. Wishful thinking would inevitably come and bite me in the
ass later.

### A barrage of issues

Testing is a thing. There is a reason Facebook spends millions to maintain a 
farm of mobile phones to test their apps on, and there is a reason why software
quality assurance is a job in and of itself. If 200 students play the game even
ten times, they've just played it 2000 times in total. The probability of a bug
popping up in those 2000 attempts is much more than it popping up in the less
than hundred or so times I ran the game. The best I could do is urge my co-TAs
to play around and stress test it (Which I don't think anyone did).

And soon, the bugs started popping up one by one. My piazza started buzzing off
the hook with bug reports, for things such as 'Sir, my program isn't compiling'
to 'Sir, the bishop is moving weirdly'. Most annoying were the followup
comments on bugs which I had fixed already, and just updating the code would
have helped. I think we also made a mistake with distribution: The starter code
was distributed via a zip on the course webpage, which linked to google drive.
To push an update, I had to package the code and upload it to google drive.
Another one of the many things I hoped to fix next time.

## Rollerball v2

For version 2, we initially planned on making it deep-learning based. We'd 
provide PyTorch bindings. All these hopes were dashed when we walked into the 
Professor's office to discuss the assignment.

> Deep Learning is taught to them only for a week, and they simply won't know 
> how to use it practically. You should have said this before.<br>
> <br>
> We'll do what we did previously: Make 3 different boards, and run 3 different 
> tournaments. I hope that's not too much work, considering your code would be
> modular as we had discussed this possibility before.

I now had to refactor and include three boards, along with a UI for them. There
goes my weekend!

### The big refactor

There was a huge checklist of things to get done. Some of these were hard 
requirements, and some were things that would be nice to have. In no particular
order, here was the list of things I got done:

- **Three Boards:** There would be a 8x4 board (8x8 with a 4x4 hole in the
  middle), and a 8x2 board in addition to the 7x3 board we already had.
  Each board would have a different tournament, and the final scores would be
  summed across all three tournaments.

- **Fixing the clock:** We'd move to giving each user a time budget, and syncing 
  the clocks at each move. This would require adding a time field in the protocol, 
  and maintaining a clock in the engine.

- **Move validation on the Arbiter:** Since we would extend the A2 arbiter for 
  move validation and since it was written in C++, we could plug in the same 
  board library. Validating the moves on the client side was no longer a
  requirement.

- **Knight moves:** We planned on introducing a Knight to the 8x2 board. The 
  knight would move in the same manner as a chess knight, and would be able 
  to jump and ignore directions. We would need to create a new piece type, 
  allocate a new bit to it and create a new method to generate moves for it.

- **Better UI:** The UI was hacky. It didn't maintain state properly, and had 
  to be reloaded and reconnected to bots every time a new game was to be 
  started. I wanted to create state machines for the connection and game in the 
  UI so that we could connect/disconnect and start games on demand.

- **More robust move generation:** Since board layouts were going to be 
  generalized, we could no longer do a hacky if-else over the squares to 
  generate moves. Cleaning up that code would also remove any hidden bugs in the 
  move generation

- **Tournament Rules:** Deciding on seeding, tournament allocations, group
  stage matchups etc. Points scoring. This was less of code and more of decision 
  making.

- **Generalized Pawn Promotion:** Each board would have it's own squares for 
  pawn promotion, and we would need to generate moves keeping that in mind. 

- **Distribution:** We'd distribute the source code over Git this time. It's 
  easier to push updates.

What followed were five days of pure coding. In a feat reminiscent to the 
[Seven days of creation][4], I spent two days doing a variable-sized board the 
right way, by creating board maps and rotation matrices for 8x8 boards.

```c++
constexpr U8 board_8_2[64] = {
    3, 2, 2, 2, 2, 2, 2, 2,
    3, 3, 2, 2, 2, 2, 2, 5,
    3, 3, 3, 2, 2, 2, 5, 5,
    3, 3, 3, 1, 1, 5, 5, 5,
    3, 3, 3, 1, 1, 5, 5, 5,
    3, 3, 4, 4, 4, 5, 5, 5,
    3, 4, 4, 4, 4, 4, 5, 5,
    4, 4, 4, 4, 4, 4, 4, 5
};

// ...

constexpr U8 cw_90_8x8[64] = {
    56, 48, 40, 32, 24, 16, 8,  0,
    57, 49, 41, 33, 25, 17, 9,  1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 28, 20, 12, 4,
    61, 53, 45, 37, 29, 21, 13, 5,
    62, 54, 46, 38, 30, 22, 14, 6,
    63, 55, 47, 39, 31, 23, 15, 7
};

// ...
```

our `BoardData` struct would now have pointers to the rotation matrices, and the 
board map and board type.

```c++
struct BoardData {
    ...

    // Variables that record the game status and configuration.
    BoardType board_type = SEVEN_THREE;
    U8 *board_mask;

    // Transformation arrays for 90, 180, and 270 degree rotations of the matrix.
    U8 *transform_array[4];
    U8 *inverse_transform_array[4];

    ...
};
```

`BoardData` also had a lot of new pieces and pawns, so we used the suffixes 
`_1`, `_2` ... instead of `_ws`, `_bs` (white square / black square). We also
had to change the `DEAD` constant from `pos(7,7)` to `0xff` because the (7,7)
square would now be in use.

The next step was cleaning up the move generation. The king move generation was
okay, using a loop around the king with a range/piece check. I copied this over 
for the knight. Rook and bishop move generation had to be rewritten almost 
from scratch, taking me a couple hours to implement and debug.

Pawn promotion was a bit trickier. I created an array to store the squares 
where pawns can be promoted, and did an inclusion check to see if the final 
position is in these two/three squares, and if the square is opposite the color.

It was mostly smooth sailing after this point. Once I was confident the moves 
were okay, I started testing other boards. Ironing out the kinks across boards 
took a day, mostly due to some annoying small things. We had to leave out 
promotions to knight in the larger board because only two bits were reserved 
for promotions in moves. I then added the time, redid the engine so that it 
inherited from the `AbstractEngine` class, and people could now modify the header 
file (something they raised on Piazza previously). Two-sided timing was also 
implemented.

Once the board was done, I moved on to redoing the UI. This took one and a half 
days, mostly because my Vue was very rusty. First course of action was to 
formalize the state, and then write the functions that would modify state. 
Once I made sure this was robust (with some logging to console), I laid out the 
UI and started tying the UI components to the code. Once the UI was done, it 
was time to integration test: I spun up two bots, and tried to disconnect and 
connect.

As usual, nothing worked the first time. Stopping the game merely stopped the 
timer, but the bots kept playing with each other. I had around a day left,
and needed to wrap this up pronto. Cue another day of frustratedly debugging 
JS, and I was finally done. I still think the UI came out very neat, supporting 
switching between three boards, a timer, and multiplayer connections across 
different machines. Most importantly, I had made this nearly from scratch, and 
I never considered myself much of a frontend designer. Being a full stack 
engineer is it's own reward :)

### Fewer bugs

This time, the release was not as turbulent. There were way fewer bugs, and most 
bugs were a consequence of student code. 

Unfortunately, impressions stick. I got the feeling that students perceived
that if a bug popped up, it was there in the TA code instead of in their code,
as there were quite a few bugs in the first iteration. Other than logistic
doubts, there were very few updates pushed this time, and I'm happy the code
stood up.

## Conclusion

This was not all that went into creating Rollerball: We had to develop TA bots,
an arbiter, an evaluation framework and finally seed and run the tournaments.
This was a team effort after all, and these things wouldn't have been possible
without the other TAs on this assignment.

I'm quite pleased with how this turned out. Was it hectic? Sure. Was there 
a better way to spend my time? Yes. I had to give up quite a bit of my life to 
make this happen. Would I do it again? Probably not. Doing it once is enough
pain. 

Every cloud has a silver lining, though. In terms of pushing my engineering
skills, very little comes close to creating, deploying and managing an
assignment like this, and I'm happy I got the chance to do so.

If you want to try your hand at this, the starter code is [here][5], and the 
assignment guidelines for [A2][6] and [A5][7] are public. Happy Hacking!

[1]: https://mi-g.github.io/jocly/examples/browser/control.html?game=rollerball-chess
[2]: https://chessboardjs.com/
[3]: https://www.chessprogramming.org/UCI
[4]: https://aniruddhadeb.com/articles/2022/seven-days-of-creation/
[5]: https://github.com/Aniruddha-Deb/rollerball-v2
[6]: https://www.cse.iitd.ac.in/~mausam/courses/col333/autumn2023/A2/A2.pdf
[7]: https://www.cse.iitd.ac.in/~mausam/courses/col333/autumn2023/A5/A5.pdf
