---
title: An integral involving ζ(2) (And Euler's first proof for the Basel Problem)
publishDate: '2020-04-29T22:30:00'
categories: Mathematics
slug: zeta-2-integral
---

> Evaluate the integral $$\int\_0^1 \frac{\log(x)}{x-1}dx$$

There are a few methods of doing this: the first one uses the taylor series expansion of \\( \log(1-x) \\):
$$I = -\int\_0^1 \frac{\log(1-x)}{x}dx$$ 
$$I = \int\_0^1 \frac 1x \left( x + \frac{x^2}{2} + \frac{x^3}{3} + ... \right) $$

This expression nicely integrates to give
$$I = 1 + \frac{1}{2^2} + \frac{1}{3^2} + ... = \boxed{\frac{\pi^2}{6}}$$

The last step here involves the summation \\( \zeta(2) = \sum\_{k=1}^{\infty} \frac 1 {k^2} = \frac{\pi^2}{6}\\). This summation is known as the [Basel Problem](https://en.wikipedia.org/wiki/Basel_problem) (more on this later). For now, we'll use this as a fact and move forward.

Another solution that does not involve the taylor series requires some substitutions and limit evaluation.

$$\begin{gather}
I = \int\_0^1\frac{\log x}{x-1} dx= -\int\_0^1\log x(1+x+x^2+...)dx \\\\
= -\int\_0^1 \log x \sum\_{r=0}^\infty x^r dx \\\\
= -\sum\_{r=0}^\infty\int\_0^1x^r \log x dx 
\end{gather}$$

let \\(\log x = t \implies dx = e^t dt\\):
$$\begin{gather}I = -\sum\_{r=0}^\infty \int\_{-\infty}^0te^{(r+1)t}dt \\\\
=-\sum\_{r=0}^\infty \left[\frac{te^{(r+1)t}}{(r+1)} - \frac{e^{(r+1)t}}{(r+1)^2}\right]\_{-\infty}^0\\\\
= \sum\_{r=0}^\infty \left[\frac{1}{(r+1)^2} + \lim\_{t \to -\infty} \frac{(t(r+1)-1)e^{(r+1)t}}{(r+1)^2} \right]\\\\
= \sum\_{r=0}^\infty \left[\frac{1}{(r+1)^2} - \lim\_{t \to \infty} \frac{(t(r+1)+1)}{e^{(r+1)t}(r+1)^2} \right] \\\\
= \sum\_{r=0}^\infty \left[\frac{1}{(r+1)^2} - \lim\_{t \to \infty} \frac{r+1}{e^{(r+1)t}(r+1)^3} \right] \\\\
= \sum\_{r=0}^\infty \frac{1}{(r+1)^2}\\\\
= \sum\_{k=1}^\infty \frac{1}{k^2}\\\\
\boxed{I = \frac{\pi^2}{6}}
\end{gather}$$

This solution also involves the same summation. There is, however, a solution that does not involve the summation: The general form of this integral is known as [Spence's Function](https://en.wikipedia.org/wiki/Spence%27s_function) or Dilogarithm. It's a transcendental function which has the values \\( Li\_2(0) = 1 \\) and \\( Li\_2(1) = \zeta(2) = \frac{\pi^2}{6} \\). If you know these values beforehand, you can cut out the lengthy calculation.

Back to the Basel Problem, and a bit of a primer first. The [Riemann-Zeta](https://en.wikipedia.org/wiki/Riemann_zeta_function) function is a mathematical function that is defined as \\( \zeta(s) = \sum\_{n=1}^\infty \frac{1}{n^s} \\). Thus, a convenient way of referring to the sum \\( \sum\_{k=1}^{\infty} \frac{1}{k^2} \\) would be \\( \zeta(2) \\), which I will use hereon. The quest for the value of \\( \zeta(2) \\) far predates the Riemann-zeta function (and Bernhard Riemann himself for that matter). This problem was first posed by Pietro Mengoli, an Italian mathematician who had proved that the harmonic series \\( \left( \sum\_{n=1}^{\infty} \frac 1n \right) \\) diverges and also found the value of the sum \\( \sum\_{r=1}^\infty (-1)^{r-1} \frac 1r \\) to be \\( \log(2) \\). The problem is called the Basel problem as Basel in Switzerland is the hometown of Euler, who solved the problem and the Bernoulli family, who unsuccessfully attacked the problem.

The story goes that the first proof Euler gave was not accepted as it involved an unproven factorization of \\( \sin(x) \\). Euler being Euler, gave a second proof and a third proof as well, which were accepted. The initial proof is as follows: From the taylor series expansion of \\( \sin(x) \\), we have
$$\sin(x) = x + \frac{x^3}{3!} + \frac{x^5}{5!} + ... $$

\\( \sin(x) \\) can also be written as a function of it's roots, according to the [Weierstrass Factorization Theorem](https://en.wikipedia.org/wiki/Weierstrass_factorization_theorem). Note that this theorem was published a 100 years after Euler's proof, which is why Euler's proof was initially not accepted. Euler factorized \\( \sin(x) \\) as follows:
$$\sin(x) = x(1 - \frac x\pi)(1 + \frac x\pi)(1 - \frac{x}{2\pi})(1+\frac{x}{2\pi})...$$ $$\sin(x) = x(1-\frac{x^2}{\pi^2})(1-\frac{x^2}{4\pi^2})... \tag{1}$$

Why did Euler choose to factorize \\( \sin(x) \\) as such? He could also have chosen the function \\(x(x-\pi)(x+\pi)(x-2\pi)(x+2\pi)...\\). A simple trick I used to explain this is that the function chosen by Euler is bounded and also converges to a common limit. Dividing both sides by \\( x \\) and evaluating the limit \\(lim\_{x \to 0} \frac{\sin(x)}{x}\\) in equation \\( (1) \\), we see that both sides converge to 1.

Back to the proof, since we have two equivalent representations of \\( \sin(x) \\), all we have to do is compare the coefficients of \\( x^3 \\) in both of them to find the value of \\( \zeta(2) \\)
$$\frac{1}{3!} = \frac{1}{\pi^2} \sum\_{k=1}^{\infty} \frac{1}{k^2}$$
$$\boxed{\sum\_{k=1}^{\infty} \frac{1}{k^2} = \frac{\pi^2}{6}}$$

This completes the proof. A really beautiful and simple proof, this was the one of the two proofs (Along with [Cauchy's proof](https://en.wikipedia.org/wiki/Basel_problem#Cauchy's_proof)) that I was able to understand. For more proofs involving higher order mathematics, you can check out the links [here](http://math.cmu.edu/~bwsulliv/basel-problem.pdf) and [here](https://math.stackexchange.com/questions/8337/different-methods-to-compute-sum-limits-k-1-infty-frac1k2-basel-pro).
