Title: Is the shortest solution to a problem the best?
Date: 2020-07-26 21:00
Category: Mathematics
Tags: Mathematics
Slug: shortest-solution-best-or-not

My old man always used to say that there are two ways to solve a problem: there's 
the horse way, and there's the donkey way. The donkey way involves tedious 
calculations, whereas the horse way 'cuts' through the problem. Take this problem
as an example:

> For each positive integer $n$, let $$y\_n = ((n+1)(n+2)...(n+n))^\frac1n$$ for
> $x \in \mathbb{R}$. Let $[x]$ be the greatest integer less than or equal to $x$. 
> If $\lim\_{n \to \infty} y\_n = L$, then the value of $[L]$ is \_\_\_\_\_\_ ?

This problem is taken from the JEE(A) 2018 Paper 1 Math section. There are two 
ways of doing this: the first one is the naive, or donkey way:
$$\begin{gather}
L = \lim\_{n \to \infty} \left((1+\frac1n)(1+\frac2n)....(1+\frac nn)\right)^\frac1n \\\\
\log L = \lim\_{n \to \infty} \frac{1}{n} \sum\_{r=0}^n \log\left(1+\frac rn\right) \\\\
\log L = \int\_0^1 \log(1+x)dx \\\\
\log L = (1+x)\log(1+x) - x |\_0^1 \\\\
\log L = 2\log2 - 1 \\\\
L = \frac{4}{e} \\\\
\boxed{[L] = 1} \\\\
\end{gather}$$

It looks simple, because I've made it look simple. The integration by parts step
is time consuming, as well as the substitution and conversion into Riemann sum.
They're all simple steps, but quite lengthy when done in succession. This is 
how we are taught to approach most problems: do the steps to yield an answer. 
Here's an example of the 'horse' way:
$$\begin{gather}
(1+0)(1+0)(1+0)...(1+0) < (1+\frac1n)(1+\frac2n)...(1+\frac nn) < (1+1)(1+1)(1+1)...(1+1) \\\\
\lim\_{n \to \infty} 1^\frac1n < \lim\_{n \to \infty} \left((1+\frac1n)(1+\frac2n)....(1+\frac nn)\right)^\frac1n < \lim\_{n \to \infty} 2^{n \cdot \frac1n} \\\\
1 < L < 2 \\\\
\boxed{[L] = 1}
\end{gather}$$

And we're done! Simple application of sandwich theorem gives us the answer here
to the required accuracy. Looking at both techniques, the way of the horse 
always seems smarter and more elegant than the way of the donkey... or does it?
Here's an example of another problem:

> If 
> $$a = 1 + \frac{x^3}{3!} + \frac{x^6}{6!} + \frac{x^9}{9!} + ...$$
> $$b = x + \frac{x^4}{4!} + \frac{x^7}{7!} + \frac{x^{10}}{10!} + ...$$
> $$c = \frac{x^2}{2!} + \frac{x^5}{5!} + \frac{x^8}{8!} + \frac{x^{11}}{11!} + ...$$
> the value of $a^3 + b^3 + c^3 - 3abc = ?$

This looks like an interesting problem. The horse way of doing this would be to
first make a (perfectly valid) assumption that the answer is independent of $x$, 
because the answer is a constant and if it was dependent on $x$, it would be 
of the form $f(x)$, which it clearly isn't. Since it is independent of $x$, 
let $x=0$, giving us $a=1, b=0, c=0$. Thus, $a^3 + b^3 + c^3 - 3abc = 1$, which
is the correct answer.

This solution looks good, but it is hacky at best and incomplete at worst. 
Note that the problem setters have not defined the domain of $a,b,c$. An interesting
twist would have been if $x \in \mathbb{R}^+$, then this hack would have been 
[defenestrated](https://www.google.com/search?q=defenestrated). Here, the donkey method, though longer, 
is more elegant and meaningful than the horse method. To solve this the right 
way, recall the identity
$$a^3 + b^3 + c^3 - 3abc = (a+b+c)(a+b\omega+c\omega^2)(a+b\omega^2+c\omega)$$
where $\omega$ is the complex cube root of unity.
If we substitute $a,b,c$ in the RHS and use the taylor expansion of $e^x$, then 
we get:
$$e^x \cdot e^{x\omega} \cdot e^{x\omega^2}$$
this is the same as $e^{x(1+\omega+\omega^2)}$, and, as $1 + \omega + \omega^2 = 0$,
the final answer is 
$$e^{x \cdot 0} = \boxed{1}$$

This is The Right Way<sup>TM</sup> of solving the problem. Even though it is 
the lengthier, more mentally strenuous way, this is a case where the 'donkey'
method is more elegant than the 'horse' method.
