---
title: A Good JEE Main (September) problem
publishDate: '2020-09-11T09:01:00'
categories: Mathematics
tags:
- Mathematics
- JEE
slug: good-jee-main-problem
draft: true
---

This beauty came in the 2nd September shift 2 paper:
> Let $A = \\{ X = (x, y, z)^T : PX = 0 \text{ and } x^2+y^2+z^2=1 \\}$, where 
> $$P = \left[ \begin{array}{l l l}1&2&1 \\\\ -2&3&-4 \\\\ 1&9&-1 \end{array}\right]$$
> then the set A:
>
> 1. is a singleton
> 2. is an empty set
> 3. contains exactly two elements
> 4. contains more than two elements

This is a great problem, one that should have featured in advanced rather than 
main. It involves matrices and 3D Geometry and fits in to linear algebra more 
than any other topic.

To solve this, notice that $A$ is a set of column vectors which lie on the intersection
of the three planes determined by $PX = 0$. The three planes are:
$$\begin{align}
x + 2y + z &= 0 \\\\
-2x + 3y - 4z &= 0 \\\\
x + 9y - z &= 0 \\\\
\end{align}$$

These three planes have a trivial solution $x = y = z = 0$. Let's see if they
have non-trivial solutions by obtaining $det(P)$:
$$\begin{align}
|P| &= \left| \begin{array}{l l l}1&2&1\\\\ -2&3&-4\\\\ 1&9&-1\end{array} \right| = -3 -8 -18 -3 +36 -4 \\\\
|P| &= 0 \\
\end{align}$$

Thus, they have non-trivial solutions. All the planes are concurrent and form a 
line that passes through origin. Thus, if $S = \\{ X = (\lambda\_1x,\\  \lambda\_2y,\\  \lambda\_3z)^t : 
\lambda\_1,\\  \lambda\_2,\\  \lambda\_3 \in R \\}$ is the line formed by the planes, 
then S has only two elements for which the magnitude of $X$ is 1. These two elements
are the only elements of $A$, thus $A$ contains exactly two elements. $\blacksquare$

A great problem, that required good thinking and visualization skills. The JEE
was a toss-up between great problems like this and stupid ones like this:

> If you spill a chemical toilet cleaning liquid on your hand, your first aid 
> would be : 
>
> 1. vinegar
> 2. aqueous $\ce{NH3}$
> 3. aqueous $\ce{NaHCO3}$
> 4. aqueous $\ce{NaOH}$

Here's to hoping the JEE advanced has better chemistry problems :)
