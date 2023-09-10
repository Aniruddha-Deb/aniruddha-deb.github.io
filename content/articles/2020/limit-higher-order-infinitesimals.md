---
title: Limit involving higher order infinitesimals
publishDate: '2020-06-05T07:30:00'
categories: Mathematics
tags:
- Mathematics
slug: limit-higher-order-infinitesimals
---

Simple limit problems consist of the form $\lim\_{x \to 0}\frac{O\_1(x)O\_2(x)..}{O\_a(x)O\_b(x)..}$, such as $\lim\_{x \to 0} \frac{\sin 3x \tan 2x \tan^{-1} 5x}{x^2 \ln(1+x)}$. Here, the infinitesimals are well defined and cancel out easily. Some trickier limit problems involve the difference of two infinitesimals. A good example is $\lim\_{t \to 0} \frac{\sin t - \tan t}{t^3}$. These kind of problems require expansions to solve them cleanly. L'Hopital rule is tedious as it will need to be repeated atleast thrice for this given limit, which involves infinitesimals of order 3. To illustrate how to solve these problems, I'll give a trickier example:

> Evaluate the limit $$\lim\_{n \to \infty} \left( e - \left( 1 + \frac1n \right) ^n \right) ^\frac 1n$$

It's easy to assume that the limit $\lim\_{n \to \infty} \left( 1 + \frac1n \right)^n$ evaluates to $e$, which means that the expression inside the outer brackets would tend to zero, giving the answer as zero. However, all is not as it seems. This is a good example of difference between infinitesimals yielding a higher order infinitesimal. To start with, consider the function
$$f(n) =  \lim\_{n \to \infty} \left( 1 + \frac1n \right)^n$$
Taking a logarithm both sides and using a taylor series expansion for the log on the right side gives
$$\begin{gather}
\log f(n) = \lim\_{n \to \infty} n \left( \frac1n - \frac 1{2n^2} + O\left(\frac 1 {n^3}\right) \right) \\\\
f(n) = \lim\_{n \to \infty}e^{1 - \frac 1{2n} + O\left(\frac 1 {n^2}\right)}
\end{gather}$$

If we substitute $f(n)$ in the limit now, we can see that
$$L = \lim\_{n \to \infty} \left( e \left( 1 - e^{-\frac 1{2n} + O\left(\frac 1 {n^2}\right)}\right) \right) ^\frac 1n$$

Taking a logarithm both sides gives us
$$\log L = \lim\_{n \to \infty} \underbrace{\frac{1}{n}}\_{f\_1} + \underbrace{\frac{ \log\left( 1 - e^{-\frac 1{2n} + O\left(\frac 1 {n^2}\right)}\right)}{n}}\_{f\_2}$$

$f\_1$ is trivially $0$. $f\_2$ can be evaluated using L'Hopital rule, which gives
$$f\_2 = \lim\_{n \to \infty} \frac{\frac{1}{2n^2} + ... }{1 - e^{-\frac 1{2n} + O\left(\frac 1 {n^2}\right)}}$$

This evaluates to $0$ as the numerator is a higher order infinitesimal than the denominator. Thus, we have
$$\log L = 0$$

Taking an exponent both sides gives us
$$\boxed{L = 1}$$
