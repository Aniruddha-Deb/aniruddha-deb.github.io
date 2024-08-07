---
title: A Note on Conditional Probability
publishDate: '2021-12-25T15:20:00'
categories: Mathematics
tags:
- Mathematics
slug: note-on-conditional-probability
---

$\newcommand{\cE}[2]{\mathbf{E}(#1\ |\ #2)}$$\newcommand{\cP}[2]{\mathbf{P}(#1\ |\ #2)}$$\renewcommand{\P}[1]{\mathbf{P}(#1)}$$\newcommand{\E}[1]{\mathbf{E}(#1)}$$\newcommand{\F}{\mathcal{F}}$$\newcommand{\G}{\mathcal{G}}$$\newcommand{\ind}[1]{\mathbf{1}\_{#1}}$
To motivate this note, I’ll pose the following problem:

> Consider $X \sim \text{Uniform}([0,1])$. What is $\cP{X > \frac{1}{2}}{X \in \mathbb{Q}}$ ?

At first glance, the answer seems simple: it’s 1/2! Closer inspection reveals that the event $X \in \mathbb{Q}$ is not measurable: the rationals have measure zero, hence from our high-school (perhaps even undergraduate) definition of conditional probability, the given probability should be undefined. However, the conditional probability does exist, and it equals 1/2.

## Redefining Conditional Probability

To account for events of measure zero, we must first redefine $\cP{A}{B}$. So far, we've defined this as $\cP{A}{B} = \P{A \cap B}\ /\ \P{B}$, $\P{B} \ne 0$. We overcome the case where $\P{B} = 0$ by defining **conditional probability as a random variable that satisfies some properties**. The intuition behind this is that if the conditional probability doesn't exist by the previous definition, we can use expectation to say that it 'might' exist and be equal to some expected value. This also nicely sets us up for conditional expectation and variance, and the law of total expectation and law of total variance. Before formally defining conditional probability, Recall the following definitions first:

> **Definition**: A Sub-$\sigma$ algebra of $\F$ is a $\sigma$ algebra $\G$ such that $\G \subset \F$

> **Definition**: A Measurable Function $f: (X,\Sigma) \to (Y,\Gamma)$ between two measurable spaces is a function such that for every $E \in \Gamma$, $\\{x \in X\ |\ f(x) \in E\\} \in \Sigma$. If $(Y, \Gamma) = (\mathbb{R}, \mathcal{B}(\mathbb{R}))$, then $f$ is said to be $\Sigma$-measurable

> **Definition**: The $\sigma$-algebra generated by a function $f: (X,\Sigma) \to (Y, \Gamma)$ is the collection of all inverse images $f^{-1}(S),\ S \in \Gamma$. 
$$\sigma(f) := \\{ f^{-1}(S) : S \in \Gamma \\}$$

With these three definitions, we define the conditional probability function on a sub-$\sigma$ algebra $\G$ as follows:

> **Definition**: The conditional probability $\cP{\cdot}{\G}$ is a $\G$-measurable random variable such that $$\E{\cP{A}{\G}\ind{G}} = \P{A \cap G} \quad \forall\ G \in \G$$ In terms of integrals, we can rewrite this as $$\int\_G \cP{A}{\G} d\mathbf{P} = \P{A \cap G}$$

Defining the conditioning on a sub-$\sigma$ algebra rather than an event or another random variable has the following benefits:

* If we want to condition on a random variable $X$, then $\G = \sigma(X)$
* If we want to condition on multiple random variables $X\_1, X\_2, \ldots$, then $\G = \sigma(X\_1, X\_2, \ldots)$ where $\sigma(X\_1, X\_2) = \\{ \\{X\_1 \le a\\} \cap \\{X\_2 \le b\\}\ |\ a,b \in \mathbb{R}\\}$ (can be extended to a countable sequence of random variables)

Therefore, this definition of conditional probability is the most general definition.

## Existence and Uniqueness of Conditional Probability

From the integral definition, it may be obvious that **conditional probability is unique up to a set of measure zero**, that is, if $\P{A} = 0$, then $\cP{A}{\G}$ can take any value. This leads to the problem of *regularized conditional probability*. Essentially, we define values for sets whose measure is zero such that the resulting conditional probability function is 'nice', ie measurable. This would need us to set up constructs such as a [Polish Space](https://en.wikipedia.org/wiki/Radon_space) and then use some functional analysis results, but we'll not get into that in this article.

Existence can be proved in many ways: here, we use the Radon-Nikodym theorem. I won't be proving the theorem, but I'll quote it, along with some exposition, which should be sufficient.

> **Definition**: A measure $\mu$ is said to be _absolutely continuous_ with respect to another measure $\lambda$ (both defined on the same $\sigma$-algebra) if for every measurable set $A$, $\lambda(A) = 0 \implies \mu(A) = 0$. We denote this as $\mu \ll \lambda$, and we say that $\lambda$ _dominates_ $\mu$

> **Theorem (Radon-Nikodym):** if $\mu$ and $\lambda$ are defined on $(X,\Sigma)$ such that $mu \ll \lambda$, then there exists a $\Sigma$-measurable function $f$ such that for any $A \in \Sigma$, $$\mu(A) = \int\_A f\ d\lambda$$
The function $f$ is called the _radon-nikodym_ derivative of $\mu$ and is denoted as $d\mu/d\lambda$.
  
We now prove our claim

> **Claim:** $\cP{A}{\G}$ exists and is unique upto a set of probability 0

**Proof:** Define $\cP{A}{\G}$ to simply be $d\nu/d\mathbf{P}\_\G$, where $\mathbf{P}\_\G$ is simply $\mathbf{P}$ restricted to $\G$, and $$\nu(E) = \P{A \cap E}$$ Note $\nu \ll \mathbf{P}\_\G$ and by the radon-nikodym theorem, $\cP{A}{\G}$ exists and is unique upto a set of probability 0. Note that defining $\cP{A}{\G}$ like so also takes care of the definition, as $$\E{\cP{A}{\G}\ind{G}} = \int\_G \frac{d\nu}{d\mathbf{P}\_\G}\ d\mathbf{P}\_\G = \nu(G) = \P{A \cap G}$$

## Conditional Expectation, and deriving Conditional Probability from Conditional Expectation

Conditional expectation is defined in much the same way: as a random variable satisfying the property $\E{\cE{Y}{\G}\ind{G}} = \E{Y \ind{G}}$. In a handwavy sense, conditional expectation is 'the best approximation' of the specified quantity, given the information we have from $\G$. There's a very nice functional analysis proof of this which treats random variables as vectors in a functional space and then approximates them using expectation, but I'll leave that out for now.

Most of the same properties as conditional probability apply to conditional expectation as well, just that in the proof of existence, since expectation can be negative and we need a positive value for it to be a measure, we define $\cE{A}{\G}$ as $d\E{A^+ \ind{G}}/d\mathbf{P}\_\G - d\E{A^- \ind{G}}/d\mathbf{P}\_\G$ and proceed similarly. 

In several textbooks, conditional expectation is derived first, and conditional probability follows. This is because $\cP{A}{\G} = \cE{\ind{A}}{\G}$. Also, a neat proof involving functional analysis is used to prove the existence of conditional expectation: $\cE{Y}{\G}$ is the orthogonal projection of $Y$ onto the closed subspace $\mathbb{L}^2(\G)$, and from results about hilbert space, we can prove this.

## The Problem

Now that we have this definition, how do we apply it? Sadly, we can't directly obtain the conditional probability from it (unless we evaluate the radon-nikodym derivative), and the best we can do is assume that the conditional probability is a reasonable random variable, and then verify that it satisfies the definition.

For the given problem, $\G = \sigma(\mathbb{Q})$. This is because for $\cP{\\{X > x\\}}{\G}$ to be $\G$-measurable, $G$ must have all the information we're given, namely whether $X$ is rational or not, hence the specification of the sub-$\sigma$ algebra as mentioned. You can also think of it from the best approximation perspective: we're only given information about whether X is rational or not and about X's magnitude, and both those quantities are expressed in this sub-$\sigma$ algebra. Now, let $\cP{\\{X > x\\}}{\G} = 1-x$. This is $\G$-measurable (the preimage of any borel set lies in $\G$). Verifying the two integrals gives us
$$\begin{align}
\P{\\{X > x\\} \cup G} &= \int\_G \int\_x^1 1\ d\mathbf{P}\ d\mathbf{P\_0}\\\\
&= \int\_G 1-x\ d\mathbf{P\_0}
\end{align}$$
$$\E{\cP{\\{X > x\\}}{\G}\ind{G}} = \int\_G 1-x\ d\mathbf{P\_0}$$
Since both these integrals are equal for all $G \in \G$, we have $\cP{X > \frac{1}{2}}{X \in \mathbb{Q}} = 1/2$.

### References:

1. Rosenthal, Jeffrey S. _A First Look at Rigorous Probability Theory_. 2nd ed, World Scientific, 2006.
2. [https://math.stackexchange.com/questions/2306986/uniqueness-of-conditional-expectation](https://math.stackexchange.com/questions/2306986/uniqueness-of-conditional-expectation)
3. [https://stats.stackexchange.com/questions/395310/what-does-conditioning-on-a-random-variable-mean](https://stats.stackexchange.com/questions/395310/what-does-conditioning-on-a-random-variable-mean)
4. [https://www.stat.berkeley.edu/users/pitman/s205f02/lecture15.pdf](https://www.stat.berkeley.edu/users/pitman/s205f02/lecture15.pdf) (this contains the projection proof)
5. [http://www.stat.cmu.edu/~arinaldo/Teaching/36752/S18/Notes/lec\_notes\_6.pdf](http://www.stat.cmu.edu/~arinaldo/Teaching/36752/S18/Notes/lec_notes_6.pdf) (this too has the projection proof)
6. Billingsley, Patrick. Probability and Measure. 3rd ed, Wiley, 1995.

### PS

Merry christmas to you if you're reading this! A junior emailed me a while back, stating that he read my blog and couldn't grasp at times why there are _random mathematical stuffs_. In my reply, the blog was supposed to be a math/programming blog with the occasional _random personal stuff_, but the tables seem to have turned :P

I think a good new year's resolution would be to learn one new math topic every week and then blog about it. Technical blogging as of now takes a lot of time for me (this article took the good part of a day), and I think as I write and learn more, that time should go down. 

Here's to a more mathematical 2022!
