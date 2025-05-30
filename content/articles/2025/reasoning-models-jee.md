---
title: "Reasoning models obtain a top 10 rank in JEE Advanced 2025"
date: 2025-05-30T19:00:00+05:30
---

Last Updated: 30 May 2025  
[Code on GitHub](https://github.com/Aniruddha-Deb/jeebench25)

## Introduction

My holiday coincided with the JEE(A) 2025 paper, and I was curious to see how 
far along we are on the AI extinction timeline. This post presents JEEBench25, 
a dataset containing all 96 questions of the [2025 JEE Advanced paper][JEEA]. 
[Daman and Himanshu][JEEBench], ex-DAIR student researchers had previously
curated problems ignoring images due to the lacking multimodal capabilities of 
SoTA models of the time. JEEBench25 includes images for all the questions on 
the test. Evaluation of OpenAI models (which anyone can pay $20 to access) on 
this dataset show o4-mini gets **All India Rank 8 with 319/360 marks**, while 
o3 gets **All India Rank 10 with 315/360 marks**. This puts them in the **top 
99.995% of students attempting the exam**. 

While such results are not entirely surprising due to the performance of these 
reasoning models on [MathArena][MathArena] benchmarks with similarly difficult 
questions, this is the first uncontaminated evaluation on (1) an examination 
that is not purely math-oriented, and (2) A high-stakes 
exam used for college/programme allotment. The high scores of these publicly 
accessible models raise questions regarding the validity of high-stakes 
examinations as a tool for assessing student talent.

## Dataset

The Dataset was curated from the question papers and provisional answer keys 
available on the offical [JEE(A) 2025 webpage][JEEA]. Ranges are specified for 
numerical type questions, the same as the ones in the answer key, and answers 
corresponding to those ranges are marked correct.

There are two questions with answers that don't fit in a range: Q11 of Physics paper 1 
(0.5 OR 0.75) and Q11 of Chemistry paper 1 ([-29.95 to -29.8] OR [29.8 to 29.95]). 
The OR syntax is used to specify these answers (for example, 
`[-29.95,-29.8]|[29.8,29.95]`) so these are also supported by the evaluator.

There was only one bonus question in the provisional answer key (an incorrect
question to which everyone gets marks) - Question 4 of the Physics section in 
Paper 2. I've marked bonus questions with the answer `BONUS` in the dataset.

## Evaluation

The prompts are organized as jinja templates corresponding to each question type. The templates
provide scoring guidelines for each question which are in-line with the ones 
presented in the actual paper. The templates also give the model an option 
to skip questions with negative marks for incorrect answers by replying with an 
O instead of A,B,C or D.

For non-reasoning models like gpt-4o, I've used a developer prompt that encourages problem solving.
The developer prompt tells the model that it is a gifted olympiad medalist and 
a prior single-digit ranker in the exam, and now it has the knowledge of more 
advanced mathematical/physical tools which it may use in addition to it's stellar 
problem solving skills. The prompt is zero-shot, i.e. there are no examples 
of solved problems. Adding examples may improve accuracy but make the runs more 
expensive. For reasoning models, I've skipped this developer prompt 
according to the OpenAI prompting guidelines for reasoning models and provided 
only the problem statement with problem instructions.

## Results

| Model   | Paper | Paper Total (180) | Total (360) |  Math (60) | Physics (60) | Chemistry (60) |
|---------|-------|-------------------|-------------|------------|--------------|----------------|
| gpt-4o  | P1    | 76                | 136         |  27        | 17           | 32             |
|         | P2    | 60                |             |  15        | 11           | 34             |
| o4-mini | P1    | **155**           | **319**     |  57        | 53           | 45             |
|         | P2    | **164**           |             |  60        | 52           | 52             |
| o3      | P1    | 153               | 315         |  56        | 45           | 52             |
|         | P2    | 162               |             |  53        | 56           | 53             |

All runs were on the medium reasoning setting. The cost and duration of 
the runs are specified below:

| Model   | Paper | Cost   | Duration  |
|---------|-------|--------|-----------|
| gpt-4o  | P1    | $0.471 | -         |
|         | P2    | -      | 10m 18s   |
| o4-mini | P1    | $0.558 | 22m 39s   |
|         | P2    | $0.567 | 24m 7s    |
| o3      | P1    | $6.483 | 54m 0s    |
|         | P2    | $7.483 | 1h 3m 58s |

The cost of the gpt-4o P2 run was not logged as I was not logging output tokens,
and the duration of the gpt-4o P1 run is indeterminate as the script broke when
processing the physics section images and had to be fixed, so the run was 
performed in two iterations. There was also a 2 to 5 second interval between 
each question, hence subtracting 4 minutes from the evaluation time is a more 
accurate estimate (subtract 1m 36s for gpt-4o)

These scores place o4-mini **eighth** and o3 **tenth**, according to data from 
[JEE 2025 Scorecard][J2025Scorecard].

### Error Analysis

[Su et al][ReasoningLength] show that reasoning models are likely to spend more 
tokens when the resulting answer is incorrect. My results agree with this claim. 

| Model   | Paper | Output Tokens per correct Q | Output Tokens per incorrect Q |
|---------|-------|------|------|
| o4-mini | P1    | 2388 | 3352 |
|         | P2    | 2457 | 4070 |
| o3      | P1    | 2852 | 5413 |
|         | P2    | 3141 | 9400 |

The output tokens per question are significantly higher for incorrect questions.
In addition, even when presented with the ability to answer O and skip the 
question, the models will reply with an incorrect answer. There was only one 
O from o4-mini in P2, and no O's from o3. [Fu et al][MCQLLM] have similar results 
but they use non-reasoning models.

## Implications

The results show that high-stakes high school examinations are no longer a hurdle 
for LLMs to solve. This is good news for students: your doubts 
will be resolved quicker, easier and faster. All it needs is access to GPT. This 
is also bad news for edtech startups such as 
[DoubtNut][DoubtNut] and other platforms, because if an on-demand model can 
solve any hard question, students will not use the platform. I don't believe 
the multibillion-dollar coaching industry is at any danger because the payee 
is the parent and not the student, so parents would continue to pay in order to 
obtain peace of mind. However, the barrier to gaining skill and 
learning is now extremely low, and anyone with a GPT subscription and sufficient
motivation will be able to do wonders.

There is also a flip side to these benefits. The current mechanism of conducting 
the JEE is via a computer-based test organized via TCS using their iON software. 
This test is conducted in exam centres that are either run by TCS or have an 
agreement with TCS to run the software. Let's call an exam centre a third-party 
centre if it's not run by TCS itself, 
i.e. doesn't have TCS or iON in the name. We also call an exam centre 
non-educational if the centre is not located in a school, university, institution,
college, academy etc. Out of the 727 centres used to conduct JEE(A) 2024, 
**133 were third-party and non-educational**. Most of these were located in Tier 2 
or Tier 3 cities. o4-mini can solve the paper as fast as you can type the 
questions in. I'm not going to make any claims here, but you see where this 
argument is going.

## Acknowledgements

Thanks to [Vaibhav Seth](https://github.com/iamsecretlyflash) for helping out 
with the OpenAI credits required for this work and for comments.

---

[JEEA]: https://jeeadv.ac.in
[JEEBench]: https://arxiv.org/abs/2305.15074
[MathArena]: https://matharena.ai/
[J2025Scorecard]: https://j2025scorecard.netlify.app
[MCQLLM]: https://arxiv.org/abs/2501.09775v1
[ReasoningLength]: https://arxiv.org/abs/2505.00127v1
[JEE24Report]: https://jeeadv.ac.in/reports/2024.pdf
[DoubtNut]: https://www.doubtnut.com/
