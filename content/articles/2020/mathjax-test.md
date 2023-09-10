---
title: MathJax Test
publishDate: '2020-04-29T10:20:00'
categories: Posts
slug: mathjax-test
---

This is a test to see if MathJax works on blogger.

> For \\(\alpha, \beta \gt -1\\), find the value of \\(\lim\_{n \to \infty} n^{\beta - \alpha} \frac{1^\alpha + 2^\alpha + 3^\alpha + ... + n^\alpha}{1^\beta + 2^\beta + 3^\beta + ... + n^\beta}\\)

So we have

$$L = \lim\_{n \to \infty} \frac{n^\beta}{n^\alpha} \times \frac{\sum\_{r=0}^n r^\alpha}{\sum\_{r=0}^n r^\beta}\\
= \lim\_{n \to \infty} \frac{\sum\_{r=0}^n (\frac rn)^\alpha}{\sum\_{r=0}^n (\frac rn)^\beta}$$

The summations can now be evaluated as Riemann sums by multiplying numerator and denominator by \(\frac 1n\)

$$L = \frac{\int\_0^1 x^\alpha dx}{\int\_0^1 x^\beta dx}\\
L = \frac{\beta+1}{\alpha +1}$$

Indeed it does! Looking forward to writing more mathematical posts.
