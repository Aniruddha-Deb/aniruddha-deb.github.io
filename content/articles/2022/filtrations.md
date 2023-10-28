---
title: Filtrations
publishDate: '2022-11-28T03:00:00'
categories: Mathematics
tags:
- Mathematics
slug: filtrations
---
## Recap

If you remember the [note on random variables](https://aniruddhadeb.com/articles/2021/note-on-random-variables.md), then this picks up exactly where that left off.
$\newcommand{\triple}{(\Omega, \mathcal{F}, \mathbf{P})}$$\newcommand{\P}{\mathbf{P}}$

> **Definition 1.1**: A Measurable space $(X,\Sigma)$ consists of a set $X$ and a $\sigma$-algebra $\Sigma$ defined on $X$.

Recall that a $\sigma$-algebra is simply a collection of subsets over $X$ that is closed over unions, intersections and complements.

> **Definition 1.2**: If $\mathcal{A}$ and $\mathcal{B}$ are $\sigma$-algebras defined on $\Omega$ and $\mathcal{B} \subseteq \mathcal{A}$, then $\mathcal{B}$ is a *sub $\sigma$-algebra* of $\mathcal{A}$

An example: Say we have a probability triple $\triple$ defined over the experiment of tossing two _independent, unbiased_ coins. Then, 
$$\begin{align}
\Omega &= \\{HH, HT, TH, TT\\} \\\\
\mathcal{F} &= 2^{\Omega} \\\\
\mathbf{P}(S) &= |S|/4
\end{align}$$

The role of a $\sigma$-algebra in a probability triple is to define over what events probability is defined. If we toss two coins sequentially, our probability space would be $\Omega = \\{HH, HT, TH, TT\\}$, but after tossing the first coin, we wouldn't be able to obtain the probability for events such as _Both coins show the same face_ (as we simply don't know the probability that the second coin turns up heads, or, in a more complicated setup, if the second coin's toss is correlated with the first coin's toss). An even simpler example is the state before we toss both coins: the coins are guaranteed to turn up some configuration in $\Omega$ with probability 1, but we can't pinpoint which configuration without knowing the probabilities associated with the coins. 

$\sigma$-algebras, then, give us the 'coarseness' of the type of events that we're allowed to play with. The trivial $\sigma$-algebra $\\{\emptyset, 2^{\Omega}\\}$ will give us either the event happening or not happening, and the complete $\sigma$-algebra $2^{\Omega}$ will give us the probability of every possible type of event (provided we have a suitable measure over this space).

## Filtrations

We'll now explore the concept of a _filtration_: A filtration is formally defined as follows:

> **Definition 1.3**: A filtration is a sequence of $\sigma$-algebras $\mathcal{F}\_i$ such that $\mathcal{F}\_0 \subseteq \mathcal{F}\_1 \subseteq \ldots \subseteq \mathcal{F}\_n \subseteq \ldots$

Filtrations can be finite as well as infinite. A filtration basically captures the 'coarseness' of a set of events. Consider the same example as before. We'll obtain three $\sigma$-algebras corresponding to the three states of the experiment<sup><a href="#footnote-1">1</a></sup>: no coins are tossed, one coin has been tossed and both coins have been tossed. The set of outcomes of a single coin is defined as $\Omega\_1 = \\{ H, T\\}$ and that for two coins is defined as $\Omega\_2 = \\{HH, HT, TH, TT\\}$. Then

\begin{align}
\mathcal{F}\_{0}  & =\\{ \emptyset,\Omega\_{2}\\} \\\\
\mathcal{F}\_{1}  &=\\{ \emptyset,\\{ HH,HT\\} ,\\{ TH,TT\\} ,\\{ HH,HT,TH,TT\\} \\} \\\\
\mathcal{F}\_{2} & = \left\\{ \begin{array}{c}
\emptyset,\\\\
\\{ HH\\} ,\\{ HT\\} ,\\{ TH\\} ,\\{ TT\\} \\\\
\\{ HH,HT\\} ,\\{ HH,TH\\} ,\\{ HH,TT\\} ,\\{ HT,TH\\} ,\\{ HT,TT\\} ,\\{ TH,TT\\} \\\\
\\{ HH,HT,TH\\} ,\\{ HH,HT,TT\\} ,\\{ HH,TH,TT\\} ,\\{ HT,TH, TT\\} \\\\
\\{ HH,HT,TH,TT\\}
\end{array}\right\\} 
\end{align}

Are the filtrations after these steps. Why only these? Looking at $\mathcal{F}\_1$, we can obtain probabilities for the following events:

$$\mathcal{F}\_1 = \\{ \emptyset, \underset{\text{first coin is H}}{\\{ HH, HT \\}}, \underset{\text{first coin is T}}{\\{TH, TT\\}}, \\underset{\text{first coin is H or T}}{\\{HH, HT, TH, TT\\}}\\}$$

We can also write $\mathcal{F}\_1$ as the cross product of the $\sigma$-algebra of $\Omega\_1$ with $\Omega\_1$:

$$\mathcal{F}\_1 = \underset{\text{All possibilities for the first coin}}{2^{\Omega\_1}} \times \underset{\text{Possibilities for the next coin}}{\Omega\_1}$$

This final argument lends itself to the generalization we seek: If we now have, say an infinite number of coins that we toss, then we can generate the sub $\sigma$-algebras 

$$\mathcal{F}\_i = 2^{\Omega\_i} \times \Omega\_\infty$$

This is a filtration, as we have $\mathcal{F}\_0 \subseteq \mathcal{F}\_1 \subseteq \ldots \subseteq \mathcal{F}\_n \subseteq \ldots$

## What next?

This only scratches the tip of the surface on what filtrations are and what they can do. Filtrations lend themselves well to stochastic processes (basically sequences of random variables defined on the same probability space). They are so common that we have the following definition:

> **Definition 1.4**: A _natural filtration_ of a stochastic process $X = (X\_i)\_{i=1}^n$ is defined as $\mathcal{F}\_i = \sigma(X_k | k \le i)$ (The $\sigma$-algebra generated by the random variables upto $i$).

As an exercise, try to verify that this is indeed a filtration.

Most of this work was taken from [Wikipedia](https://en.wikipedia.org/wiki/Filtration_\(probability_theory\)) and this very helpful [StackExchange thread](https://math.stackexchange.com/questions/3029823/intuition-of-sub-sigma-algebra-definition). I would've preferred a more verbose explanation in both these areas, which is why I wrote this up in case someone needs it :)

-----

<sup id="footnote-1">1</sup> Why are there not three probability triples corresponding to the three states? A philosophical explanation is that they're the same experiment, but a mathematical one is that even if we do have three triples, the sample space $\Omega$ would be the same across all three, and all three probability measures $\P$ would have to agree with each other. That is, for $S \in \mathcal{F}_1$, we cannot have $\P_1(S) \neq \P_2(S)$: the experiment remains the same (we're tossing the same coins, so this is not possible). Also, note that $\mathcal{F}_1 \subseteq \mathcal{F}_2$, so if $S \in \mathcal{F}_1$, then we'll also have $S \in \mathcal{F}_2$. Hence, it suffices to have just three $\sigma$-algebras
