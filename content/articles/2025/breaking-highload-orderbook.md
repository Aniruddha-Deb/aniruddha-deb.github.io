---
title: "Breaking the HighLoad Orderbook Challenge"
date: 2025-03-27T21:59:21+01:00
draft: true
---

For roughly 48 hours, I had the "fastest orderbook" in the world

![]()

This is not photoshopped or modified via Inspect Element. My orderbook was so 
_impossibly_ fast that it beat first place by 8000 points, on a challenge whose 
leaderboard has been open for almost four years now. The best part was _it used 
your average vector-based level order book_, not some AVX2 monstrosity optimized 
to death.

Unfortunately for this solution, it was like running a four-minute mile: once 
you did it, everyone noticed, realized this could be done and that doing this 
doesn't test how fast an orderbook is. And so the author rewrote the checker, 
and my magic trick no longer worked.

So, are you watching closely?

## The Pledge

If you're not familiar with [HighLoad](https://highload.fun), it's a site where 
you _join the community of the best software engineers and write the fastest 
code._ Think of it like kaggle but optimizing for speed and not accuracy. Matt
Stuchlik had some good explainer articles [here][2] and [here][3] on how to 
approach and solve these problems. These are very good articles. I got my
start to solving these problems from them. If you completely understand and 
break down the ideas implemented in them, you can easily break into the top 20 
in every challenge.

By now I've tackled enough challenges to have a playbook ready to approach new
problems, which roughly goes somewhat like this 

1. Create an input generator 
2. Create a candidate solution. The first solution will be really simple, and 
   will mostly just be mmap'ing the input and doing a first-pass naive algorithm.
3. Throw new ideas 
3. Profile this first pass to find hotspots. In most cases you're memory bound,
   so 
4. If profiling yields no results, analyse with uICA
5. If uICA yiel
4. If you're not #1, go back 

Coming back to this challenge, we have three main oeprations:

1. Inserts
2. Deletes
3. Buys

the first thing I had to worry about was creating
the input generator. For this, I needed to know the range each of those four 
values could take, and the rough distribution of these operations. Highload lets you 
print to stderr and will show you the first 1000ish lines, so printing summary 
statistics for the input is okay. It was easy to make counters for each value 
tracking the max and min and printing them out. I didn't need more specific 
information, such as the histogram etc.

The final interesting statistics I got were as follows:
```
qty,min,max
price,815,4109
size,20,200
pos,0,1014
shares,200,2000

inserts 590570
deletes 389379
bids 20051

size is NOT always a multiple of 10
bid is NOT always a multiple of 10

max of max caps is 18
```

Running this multiple times made me realize that 

## The Turn

There are a few obvious optimization ideas with these values:

1. Fix the number of levels to 5000 
2. Use int8's for size (with the possibility of SIMD'ing this - because 
   max of max caps didn't exceed 32 at any moment, so each level could be one
   SIMD vector)
3. Maintain only the best 1100 offers, as we never delete beyond that and buying
   1000 lots would always go through with these offers.

Idea 1 and 2 lend themselves fairly nicely to a simple level-based orderbook: have
a vector of vectors, and maintain the sum of elements in each vector. This is
also easy to SIMDify - while `__m256i`'s don't make inserts any faster,
deletes on a level can be sped up with some clever shuffling, and finding said
level could be sped up with a segment/fenwick tree. I'm not saying I did all of
this immediately, but the first iteration of a vector-based book did speed up 
my solution compared to the naive multiset-based one.

If you think about idea 3 more deeply, we would need to maintain a pointer to 
the 1100th order's level all the time in order to do a compare against it. This
pointer would need to be updated when a better offer is inserted, and I'd reckon
that would make up >95% of the inserts, because most book activity happens at 
the top of book and not deep in the book. So, we only get rid of inserting 5% 
of inserts, which is not a super-significant speed up.

In a more abstract sense, idea 3 tries to reduce the number of levels we track,
by eliminating updates we know are irrelevant to our final operation. This begs
the question, _what is the minimum set of updates I need to process if I know 
for a fact that I will buy 1000 orders at the end_. To know more about this, 
we need to know which of the 100 million offers we eventually end up buying. 
Let's give each update a unique ID (just sequentially increment a counter) and 
look at the top of book before we buy. 

We get the following results if we do so:

```
1047: [999974,77]
1048: [999964,154]
1050: [999859,56]
1054: [999846,100]
1055: [999848,144]
1056: [999844,179]
1057: [999847,41]
1060: [999947,167]
1062: [999841,107]
1064: [999954,191]
1070: [999839,54]
1073: [999999,44]
1085: [999949,71]
1087: [999865,24]
1098: [999943,66]
1107: [999869,106]
1145: [999987,180]
1155: [999927,130]
1163: [999875,62] [999892,178]
1170: [999877,29]
```

Bingo! The orders we lift are concentrated at the end. This makes sense, because
orderbooks are more fluid at the top rather than at the bottom. We now know for 
a fact that we don't have to process the first 999'000 updates - 99.9% of 
the data! All we have to do is this:

```
for (int i=0; i<999000; i++) {
    // read and ignore input
}
for (int i=0; i<1000; i++) {
    // read and process input
}
```

## The Prestige

We can do better.

If you profile this, you'd see that most of our time is _not_ spent updating 
the orderbook, but reading the input.

Since we don't do anything with the input, we can simply skip it when we `mmap`
the input file

```
off_t fsize = lseek(STDIN_FILENO, 0, SEEK_END);
size_t page_size = 4096;
size_t map_offset = (fsize - page_size*3) & ~(page_size - 1);
size_t map_length = (fsize - map_offset);

char* input = (char*)mmap(
    0, 
    map_length, 
    PROT_READ, 
    MAP_PRIVATE | MAP_POPULATE, 
    STDIN_FILENO, 
    map_offset
);

int i=0;
while (input[i] != '\n') i++;
i++;
while (i < map_length) {
    // read and process update
}

// buy 1000 lots and print cost
```

To test this quick-and-dirty hypothesis, I iterated over input one character at 
a time when processing it and did naive deletes and bids in my vector orderbook. 
An optimal solution would SIMD shuffle the input to decode it and use all the 
orderbook tricks I discussed above. 

My first submission had debug logging to stderr in the hot loop that I forgot 
to remove when I submitted, and it's score was <6000, 1.5x as fast as the best 
solution. Removing debug logging got me down to 1700. And at that point I opened 
the window for some fresh air.

## Concluding thoughts

```
Simple maybe, but not easy.

- Alfred Borden, _The Prestige_
```

Surprised nobody saw this, assumed the top solution(s) would be doing some 
variant of this 

Eyes on the prize. Focus on the end goal, and the rules of the system.

Checker changed. I'm a bit sad about moving goalposts - but I do this for fun and it's author's 
prerogative. Not the first time this has changed - moved from 3 to 9 submissions,
and there are debates on anybody being allowed to make testcases, testcases being
nondeterministic etc etc etc. Easy come easy go. I started solving with shared 
knowledge, and I believe knowledge should be shared.
