I try to improve the reasoning and multilingual capabilities of LLMs at IIT
Delhi, with Prof. [Parag Singla](https://www.cse.iitd.ac.in/~parags/) and Prof. 
[Mausam](https://www.cse.iitd.ac.in/~mausam). In the past, I've done some
systems programming at [Optiver](https://www.optiver.com/), and some research
at the Neuroimaging Lab with Prof. [Rahul
Garg](https://www.cse.iitd.ac.in/~rahulgarg/) before that.

Apart from this, I've worn many hats during my time at IIT Delhi, as
a [TA](https://www.cse.iitd.ac.in/~mausam/courses/col333/autumn2023/),
a [quizzer](https://qciitdelhi.netlify.app),
a [journalist](https://www.bspiitd.com) and
a [mentor](https://bsw.iitd.ac.in). When I'm not buried under coursework, I
enjoy a quick badminton match, or a round of the boardgame I'm hooked on to
(currently [riichi Mahjong](https://en.wikipedia.org/wiki/Japanese_mahjong)).

## Research Interests

I'm excited by Foundation Models, and aim to build atop
them (improving aspects such as reasoning, planning, robustness, domain
knowledge) or under them (optimizing the foundations of foundation
models, such as model serving, efficient attention mechanisms, model
quantization, and efficient inference). I am primarily interested in two key
directions:

1. **Reasoning:** Language models display a strong baseline performance across
   a variety of tasks in different domains. My experiments with these models
   lead me to believe that the lack of strong reasoning mechanisms are the only
   handicap holding these models back from becoming experts in these domains.
   **Can we find novel approaches in the form of architectural modifications** to
   transformers that can be used for reasoning tasks? Or, **can we develop a
   standardized curricula or learning regime that would help improve their
   reasoning capabilities across multiple domains and modalities**? Even if we
   improve their reasoning capabilities in a certain domain, such as math,
   **would these capabilities generalize across diverse domains**, such as
   planning, code generation, and embodied agents?

2. **Efficiency:** With the release of LLaMa, we are seeing a proliferation of
   LLM-powered personal assistants capable of running on users' devices.
   However, there is a widening gap between the hardware required to run these
   models and the hardware that is available to run these models where they are
   most required. For example, Consumer devices such as smartphones struggle to
   run inference on these models at usable speeds. I believe that solving
   on-device inference will strongly push adoption of foundation models at a
   larger scale. In this direction, I am primarily interested in **foundation
   model quantization and weight pruning**, with a focus on **making these models
   accessible and usable by everyone**. I'm also interested in optimizing these
   models for deployment on edge devices such as robots, as I believe that
   would be the primary use case for language/vision models in the near future.

Some other things I've worked on/tried out/dabbled with :

- ML and Systems: Speculative Decoding, model quantization, Low-Rank
  Adaptation, mixture of experts
- Reinforcement Learning: DQN, Policy Gradients: TRPO, PPO
- AI Safety: Alignment, Robustness (Prompt Hacking, Adversarial Attacks),
  Reward Specification, Instrumental Convergence
- Explaining ML: [[Optimizers](https://aniruddhadeb.com/articles/2023/optimizers-1/)], 
  [[Batch Normalization](https://aniruddhadeb.com/articles/2023/batch-normalization/)],
  [[L2 Regularization](https://aniruddhadeb.com/articles/2023/l2-regularization/)],
  [[Variance Estimators for Regression](https://aniruddhadeb.com/articles/2022/heteroscedastic-variance-estimation/)],
  [[Transformers](https://aniruddhadeb.com/articles/2023/properly-illustrated-transformer/)]

**I would be applying for PhD positions in the 2023-24 cycle**. If you are
accepting students and believe I would be a good fit, please do reach out.

## Quizzing at IIT Delhi

Here are some links to sets that I've (co)hosted/conducted. Will be updated as I host more sets.

{{< project 
    title="Moonman" 
    link="https://docs.google.com/presentation/d/1XUalDKMKswDNpj_mNbCHVfvIo9vbPt1iH0701RXrxN4/edit?usp=sharing"
    date="October 2022" >}}

A Music Video Quiz. I was bored of SciTech and wanted something different,
hence this quiz. First offline informal, which happened in the FACC room on a
rainy October night (don't ask why), and with cookies for most creative
incorrect answers :)

{{</ project >}}

{{< project 
    title="Rubik's Cube" 
    date="October 2021" >}}

[Prelims](https://docs.google.com/presentation/d/1rIlleNRHvl8Z24uw3gTFsqTQmoUvMOrDNA84sRUteWc/edit?usp=sharing) | [Finals](https://drive.google.com/file/d/1sd7JER8gDjK0jucvQCDSxBv5VkaCIZNg/view?usp=sharing)<br>
The first league quiz of the 2021-22 Season: Prelims are a standard slideshow,
whereas finals are the rendered slides from the final run of the program
(as such, they have two tiebreaker questions in orange and red)

{{</ project >}}

{{< project 
    title="Introduction to QC" 
    link="https://docs.google.com/presentation/d/1OsX6UVhS4xcFVlPO4STaz1ZcmBbOMPjGTA4PlqCzJqA/edit?usp=sharing"
    date="January 2022" >}}

The usual pounce/bounce introduction to quizzing, complete with google traps.
The initial setup/team asssignment/rule explanation took around an hour, after
which the other questions (mostly taken from entropy) were run for people who
stayed late

{{</ project >}}

{{< project 
    title="Entropy: A Random Quiz" 
    link="https://docs.google.com/presentation/d/1wZRMVul2y-17sAJJZraRxc9889y0ytnzBsj1DKDUXw8/edit?usp=sharing"
    date="March 2021" >}}

Entropy was the first quiz I conducted after entering IITD, and the only
fresher-hosted quiz in that year. We planned to host a prelims as well, but
didn't make it in time. Was a great experience, even though we hosted it
online.

{{</ project >}}

## Other Stuff

Some useful browser plugins to make the online sem easier: [Moodle Sidebar Plugin](https://github.com/Aniruddha-Deb/MoodleSidebarPlugin), [Impartus Ad Blocker](https://github.com/Aniruddha-Deb/ImpartusAdBlocker), [Impartus Participant Stats](https://github.com/Aniruddha-Deb/ImpartusParticipantStats), [Moodle Captcha Solver](https://github.com/Aniruddha-Deb/MoodleCaptchaSolver) (**EDIT**: Chrome is outlawing Manifest v2 to much furore, and I've officially migrated to using Firefox, along with all my plugins and scripts. You can find my UserScripts [here](https://github.com/Aniruddha-Deb/UserScripts))

[Course dependency graphs](http://aniruddhadeb.com/articles/2022/iit-course-planner-1/) for various programmes (I've been told this is what most people come here for :))

Fresher sem resources (IITD internal): [Sem 1](https://csciitd-my.sharepoint.com/:f:/g/personal/cs1200869_iitd_ac_in/Ej36n4LcTVFGnrAKpOw7i4AB1VrRvthe-TX8R4BNNRDRjw?e=Z0Edww) | [Sem 2](https://csciitd-my.sharepoint.com/:f:/g/personal/cs1200869_iitd_ac_in/EksZ_k43MuVOukNV7MAdnycBz_FINOik-uv_BC1uYP_t5Q?e=kdHDw4)

Other CS Sem Resources (IITD internal): [Sem 3](https://csciitd-my.sharepoint.com/:f:/g/personal/cs1200869_iitd_ac_in/EunTAZNCCG1DhPdfsdmwstoBxZ43PJOCP651mt3sKfKW7Q) | [Sem 4](https://csciitd-my.sharepoint.com/:f:/g/personal/cs1200869_iitd_ac_in/Er2_3xS_GX1Klx4pJde90awBJ8KfZ8RG7KvgYqk8-oQaPA?e=HuiIVS) | [Sem 5](https://csciitd-my.sharepoint.com/:f:/g/personal/cs1200869_iitd_ac_in/EngbL4fqiOFEmilT3Pu_EVEBxI2uWn657GCJJTRSZz9GQQ?e=aO0NpE) | [Sem 6](https://csciitd-my.sharepoint.com/:f:/g/personal/cs1200869_iitd_ac_in/EjHHwCa9tE9Enyg_ocwAkmIBRJnRD0SXNQU-LyCEf1SfWw?e=Ny8BgB)

For other useful IITD Websites, check out [Aditya Singh's Webpage](https://as1605.github.io/privateweb).

MTL106 Tutorial Solutions by Rishabh [here](https://fricai.github.io/mtl106/tutorial-solutions.pdf)

A few talks I've given: [Intro to Quant Finance](https://drive.google.com/file/d/1YvKM1ka1iktR0DxHXXzZ23IacFJ7gV5h/view?usp=drive_link), [T distributions](https://github.com/Aniruddha-Deb/back_to_normal), [Cellular Automata](https://github.com/Aniruddha-Deb/automata-talk)
