---
title: "LLMs for parsing unstructured data (IIT Course Planner v2!)"
publishDate: '2024-01-12T23:00:00+05:30'
categories: Programming
tags:
- Programming
- Data
- Frontend
- LLM
slug: iit-course-planner-v2
---

Happy new year! IIT Course planner (the course dependency graphs)
used to be (and probably still is) the only reason people used to visit my 
blog. So much that it accounts for more views than any other webpage, except 
the homepage, and outdoes my next most popular article by 2x

![That's very few hits :(](/articles/2024/res/iitcp_hits.png "The total pageviews is more than I expected :)")

It's also no secret that I was working on a successor for the course planner 
for a while. The previous article had stowed the graphs right at the end, as 
an appendix of sorts, and people had to scroll down all the time. So I'll make 
that easier this time.

**TL;DR:** If you're here for the successor, go [here](https://aniruddhadeb.com/IIT_course_planner).
**It's still a work in progress.**

## Contributors?

There were 6 open things I wanted people to work on when it came to the initial 
release, which can be seen on the 
[README](https://github.com/Aniruddha-Deb/IIT_course_planner/commit/eeb29e4bfd30c79ccb9cac11f35558d95cc59ad2). 
This was committed on Mar 2, 2022 and it has been almost two years since then. 

In two years, I've got no contributors for these issues.

This is not a typo. I don't know if I should be flattered, because I did it so
nicely in the first go or if I should be disappointed because everyone except 
ES1 has access to these, and AM1/MS1 have pretty terrible diagrams because 
their courses were newly introduced. I did get one text from one interested
person to add the ES1 dependencies, but that never materialized into anything.

Not having enough motivation to get the wheels rolling on v2, I tugged at my 
ex-roommate[^1] (who is now the overall coordinator of 
[DevClub](https://devclub.in/#/)), and asked him if he could get some
interested contributors.

## Teamwork

My seventh semester was hectic, to say the least. I was trying to push a
publication out while simultaneously applying to grad school, doing courses and
TAing a course (also why I didn't blog much). While I do think I got a good
team, I barely got any time to scope out the project, do the scaffolding and
add boilerplate code so most of them could take the project forward. I think
only one guy came forward, forked my old repo and repurposed the [pipeline](https://aniruddhadeb.com/articles/2022/iit-course-planner-1/) to
work on the 2023-24 courses of study. I didn't pay much heed to this until my 
semester was over, when I realized I should probably have a look. Cloning and 
playing with the extraction code gave me some clean results. The recommmended
course extraction was not great, but I hacked something together in a few that 
seemed to work. Unfortunately, this person was busy with a wedding and then 
with other things, so Sisyphus was now carrying this rock alone up the hill.

Sisyphus, though, wanted to drop the rock and let it roll down the hill while 
he enjoyed his last few months of being an undergraduate. Aditya didn't like 
that. 

> "Kuch toh results dikha de"
> "Yaar I can give it 20 hours. I think kuch toh nikal jayega but not promising anything"

## Data pipeline

I had learnt a lot from last time, and that can roughly be summed up in 3 lines:

1. No Jupyter Notebooks
2. No XML, use JSON
3. Manual labour where neccessary, LLMs where impossible

So the first task was porting the pipeline from Jupyter to bash, and exporting
the details to JSON files. I drew up a small schema and got the data saved for 
both courses and programmes to their respective JSON files.

The next step was extracting the recommended courses. I semi-automated this. 
Table recognition has advanced a bit more since the last time I wrote the 
script, and since our table had lines, [img2table](https://betterprogramming.pub/extracting-tables-from-images-in-python-made-easy-ier-3be959555f6f) 
made it easy. It wasn't perfect, though. The results still had to be manually 
verified. In hindsight, GPT-4V or LLaVa would be a good model to automate this 
process. But that's too much ML too early in the game, without good reason.

I had the course database and program data cleaned up in 5 hours, and the rest 
to kill on building the UI. While I am a better frontend engineer now than I 
was [last year](https://aniruddhadeb.com/articles/2022/rise-of-codefluencer/),
I didn't want to do frontend yet.

Which finally brings us to the title :)

## LLMs as parsers for unstructured data

TODO

## Frontend

[^1]: Final year, single rooms. Although his room is still next to mine ^_^
