---
title: "End Credits"
publishDate: '2024-05-13T00:00:00+05:30'
categories: General
tags:
- General
- Research
slug: end-credits
---

I tried to live my seventh semester like a typical grad student. Two very light
courses, Two projects heading towards publication, one course to TA and
managing my applications on the side (TOEFL/GRE/essays etc). This constitutes
standard fare for a busy PhD student, from what I've heard.

Unfortunately, I was in the driving seat for most of these things: I did a lot 
of the work on my first paper, which was a continuation of a project I had 
started last year, and also ran point on the second paper for a while. I also
had to work on an assignment and multiple quizzes for the course I was TAing.
Couple that with TOEFL/GRE prep initially, and SoP prep later on, and my
academics suffered majorly as a consequence. Most of the days at the start of
the semester were spent glued to my laptop, getting very little exercise and
not eating well.

Once September rolled around, I could see light at the end of the tunnel for 
my paper. Video game developers have something called a _crunch_ period,
wherein they put in 80-100 hour work weeks before a deadline, in order to
wrap up games. Imagine that happening every time a paper deadline rolls
around. You need to drop everything and focus on getting the paper out, no
matter where you are or what you're doing. Final touchups matter, and small
things like grammar take top priority. I was in [Japan][1]
during the ICLR deadline, and still managed to coordinate and rework a figure 
at the last minute, when everyone else was enjoying a buffet at the Indian
Embassy. I also skipped going out the day prior, in order to fair up some
results and redo a section. This is not a healthy work-life balance, and it's
hard to come to this realization if all you've done in your undergrad is 
work on assignments due at 12 AM up till the last minute. In an environment where
intellect is the only currency, the concept of having a work-life balance is 
alien. This is in stark contrast to deadlines in industry. The team I worked with 
during my intern was busy meeting one, and all of them still did normal hours,
plus an hour at most. Once the deadline was met, everyone celebrated with a
beer on Friday evening.

> "But you can't become a professor if you don't do a PhD, and one of your late-
> life goals was becoming a professor!"

If you haven't already read [Rollerball debrief][2], now is a good time to do 
so. TL;DR, creating something original takes a lot of effort and engineering 
skills. What I left out from that story, however, was the other side of the coin. 
Engineering skills are underappreciated in Academia. There was no 
motivation for going the extra mile, and at the end of the day, there seemed to 
be little to no purpose to doing this: Neither students nor the instructor 
seemed to be appreciative of the code, there was very little backing or 
sponsorship and it felt like I had to stand up and defend it at times because 
it was my idea. 

Soon, reality started catching up to me. I had not developed any specific 
skills this semester:
All I knew were the magic words to get ChatGPT to do what I wanted, and there 
was little mathematics or computer science in doing so. It was an experimental
science. Mix the reagents in the medium, put it on the boiler and come
back after six hours to check the yield, sans the nerdy goggles, lab coats and
pipettes. I was not doing any significant engineering, save for some infra to
make API calls and log runs / outputs. Moreover, I had just one semster left 
in college, and I felt like I should spend my time doing things that made me happy, 
like quizzing till 3AM, making a complex piece of software like a compiler or raytracer, 
or enjoying the little time I have left with my friends.

The other consequence of being in a fast-paced field is deciding what to keep
up with. If there are multiple breakthrough every week, but you still have to
read the three papers related to your work and implement two of
them, how much time do you spend staying up to date? Scarier still, what
happens if there is work that is too similar to what you've done, and it gets
published or put out in the open before you? What happens if the latest LLaMa 
finetune solves your open research problem? Inadvertent scooping is quite
common in such a fast-moving field, and unless you're working on something
very foundational or very left-field, there's a nonzero chance of this
happening. In this case, you have no option but to reframe and repitch your
work, lest it should go waste.

This segures nicely into peer review. Our ICLR reviews came out in early November, and I'm fairly sure
atleast one was LLM-generated. Unfortunately, this also happened to
be the review that had rated our work most highly. Two other reviews were on
the fence, and one had been unfairly critical (in our opinion), claiming that
nothing was novel while completely glossing over our most important
contribution. Sadly, this is [soon becoming the norm instead of the 
exception](https://arxiv.org/abs/2403.07183). In the
absence of concrete metrics to measure one's quality of work, things such as
your citation count, your publications, your research group and your university
become proxies of how good of a researcher you are. And each of these are biased
estimators: Peer review is clearly deeply flawed, which university you get 
into or which research group you're a part of is solely dependent on who 
you're connected to, and how many publications you have is a consequence 
of how many grad students work for you (or how lucky peer review has been for 
you, if you're a grad student). While truly good researchers have their work speak
for themselves, A mediocre researcher can masquerade as a good researcher by simply
being a prolific writer and a skilled public speaker.

> **Morell:** My talent is like yours insofar as it has any real worth at all. 
> It is the gift of finding words for divine truth.<br>
> **Marchbanks:** It's the gift of the gab, nothing more and nothing less

Opponents may argue that industry is no different: the professional world is
rife with politics, and that you need to be just as glib to rise up the
corporate ladder. I'd argue that skills matter much more in 
industry than they do in academia. I've seen senior engineers who can look at
pointers being dereferenced, and infer from the bit patterns that the pointers
are storing floats and not addresses. Even companies know it's in their best
interest to keep these engineers happy. In academia, most
professors I've met are good theoreticians, and that's where the facade
ends. They're always very busy, bad at programming or at finer details, and 
get all their ideas implemented and written up by their students, effectively 
playing the role of a manager. While this was a good end-of-life goal to 
have initially, spending more time in academia has convinced me otherwise.

But enough crying. Apart from the several problems I've mentioned above,
there are two major takeaways:

### learn the machine, don't make the machine learn.

I would recommend staying away from Machine Learning research UNLESS:

1. You have superstar advisors: either via a research intern, or through a
   recommendation, or by randomly sliding into a professor's DMs on twitter.
   Whatever works.
2. You have the patience and intuition to work in an empirical field
   which changes at the speed of light
3. You have friends and family in academia (eg your parents are CS professors)
4. You have multiple publications in A\* conferences already

I say this after throwing two of my best semesters, two research projects and
hundreds of dollars in grad school application fees at it, and still turning 
up mostly empty-handed. Granted, I also aimed disproportionately high, but 
an already unalluring academic career had to be prestigious enough to 
remotely consider over a well-paying core CS SWE job offer. And I haven't 
even gotten started about how most innovation is being driven by GPU-rich 
tech companies while academics are left to come up with low-compute party 
tricks for free.[^2]

Doing atleast one Machine Learning course is a rite of passage for a CS 
undergrad, and rightly so in this day and age. But to an undergrad 
choosing between specializing in machine learning and another field, 
and not having a significant attachment
to either field, I would recommend choosing the other field. Most importantly, 
choose an advisor with a very small research group, who collaborates with 
people outside of campus and who is willing to give you as much time as 
required.

My last pearl of wisdom in this seciton (probably very IITD-specific) would be to keep commitment 
as low as you can. A lot of advisors require you to commit for a year if they are 
to sign you up to a research project (in IITD parlance, this implies doing a BTP-2). 
Even if you are a cutthroat grade enthusiast with no life, please think twice 
before doing this. Everybody realizes how valuable their friends are in their final 
semester. If you can't make that goa trip because of your project, it will be 
incredibly hard to forgive yourself. 

### What choices do you have if you want to pursue this career?

If you are pursuing this, I'm assuming you have atleast one of the above
points ticked off. Congratulations. I've heard on the grapevine that 
professors were not taking grad students this cycle because they're 
focusing on startups. I've also seen seniors who have failed to get 
he PhD program of their choice even after a very successful MS.

Nevermind, that was quite disappointing. Truth is that the lower you aim,
the better your odds. To aim at a better ML PhD program, the best 
course of action after
a four-year undergraduate degree from an IIT is probably a MS or a predoctoral program.
Google/Microsoft's predoctoral fellows programs are both solely 
AI/ML oriented. The pay isn't too bad by SWE standards, the work is 
interesting and you get to solve challenging problems with smart people, with
the bonus of having much better prospects at a top PhD program after. Seems
like a lot of positives, and if you're considering this route, then do give
it a shot.

Another is to take a MS. While odds are about on par or better than the 
predoctoral route, you do need to pay a lot. Not to mention the missed
opportunity cost of taking this route if you already have a quant offer
already and the very marginal gains it would provide. Three semesters
or 5 quarters is not much time to learn something groundbreaking, 
especially if you've already done a lot of grad level courses during
your undergrad.

Finally, we come to a dual degree. If you're a dual degree student, 
the odds of a PhD admit significantly improve. Mostly by looking at 
seniors who've made it, around 80% of PhD direct admits were dual 
degree folks. I'd attribute it primarily to them spending more time
in the field, and by consequence having many more papers out. The 
extra year also gives you an extra summer to do a research intern,
one where you'll accomplish more by virtue of almost completing
your undergrad core.

## Conclusion

I had gotten a Mahjong set from Japan. Soon enough, my entire wing was playing 
Mahjong, and spending friday/saturday nights playing Mahjong became a habit. 
These late nights spent with comrades, who had memorized Japanese numbers 
without much complain in order to play a game that I was enthusiastic about,
made me realize the value of having friends and a life. It wasn't a concept
somewhere in the back of my mind anymore. It was all too real, and a luxury I 
would foresake in six months.

Coming home over the winter, I made peace with the low odds and decided to 
take it easy the next semester. Suddenly, I had a lot more time. I wasn't 
under pressure to achieve anything. I'd hit the gym in the mornings, attend classes, learn cool 
stuff, sit in the library and code throughout the afternoon and finally go 
running in the evenings. Over the weekends, I'd mostly quiz or find a new
restaurant to eat at in Delhi.

For the first time in a while, I had a life. And life was good. I went to 
IITKGP for Inter-IIT quizzing and then to IIMC for nihilanth, and finally
to IITB over the midsem holidays for more quizzing. I made a 
compiler and a raytracer in the same semester and won a quant 
competition somewhere in between. Most importantly, I finally spent a 
lot of time with my friends. Evenings where I didn't have anything to do 
but lounge at a friend's room and play FIFA with them after a trip to the 
night mess.

My acceptances and interviews rolled in around mid February, but I wasn't
worried at this point. I had achieved what I wanted to achieve, and obtained
the answers I had set out to find. Doing my BTP-2 in earnest would have put me 
in the running for the best B.Tech Project award, but an extra trophy or another
paper with my name on it paled in comparision to my simple joys of life.

Research is great, but it isn't for me. The key ideas in the works of 
the best researchers I've met seem simple, but they're backed by immense 
conviction, several experiments proving they work, and peer review. 
To find out if research is for you, though, 
you need to know yourself through and through very early in the game. 
This is very hard to do: you need to try out a lot of things to find the one thing you're
good at. Exploration heavily favous exploitation at the beginning of one's
career, and exploration during one's undergraduate degree is nearly zero-cost.

In conclusion, I'm happy at being given the chance to explore. I can 
wholeheartedly say that the experience was well worth
it, and I would encourage everyone to give it a shot atleast once. Who
knows, you may be an amazing researcher! However, this is (probably) where I draw the
curtain on my research journey.

Time to build something.
