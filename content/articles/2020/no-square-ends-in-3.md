---
title: No square ends in 3
publishDate: '2020-05-15T11:30:00'
categories: Mathematics
tags:
- Mathematics
slug: no-square-ends-in-3
summary: "This is an interesting number theory fact that seems strange when taken
  at face value. Here's a small proof of it:"
---

This is an interesting number theory fact that seems strange when taken at face value. Here's a small proof of it:
$$\begin{array}{|c|c|}
\hline
\text{last digit of number} & \text{last digit of square} \\\\
\hline
0 & 0 \\\\
1 & 1 \\\\
2 & 4 \\\\
3 & 9 \\\\
4 & 6 \\\\
5 & 5 \\\\
6 & 6 \\\\
7 & 9 \\\\
8 & 4 \\\\
9 & 1 \\\\
\hline
\end{array}$$

It's easy to see that no square is ending in 3 (or 2, 7 or 8 for that matter). What are the implications of this? Try the following sum:

> How many solutions of $x$ exist such that $$\sum\_{i=1}^x i! = n^2, \space n \in N$$

In simpler terms, what summations of the factorial give us a perfect square? We can work out the first few by hand
$$\begin{gather}
x = 1 \implies S\_1 = 1! = 1\\\\
x = 2 \implies S\_2 = S\_1 + 2! = 3 \\\\
x = 3 \implies S\_3 = S\_2 + 3! = 9 \\\\
x = 4 \implies S\_4 = S\_3 + 4! = 33
\end{gather}$$

For $5!$ and above, the last number is always 0. When we use the above recurrence relation for $x \ge 5$, the last digit will always be 3, and since no square ends in 3, there are only two values of $x$ for which the given equation holds, which are $1$ and $3$.  $\blacksquare$
