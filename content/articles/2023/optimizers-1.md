---
title: Optimizers, Part 1
publishDate: '2023-01-02T12:25:00'
categories: Programming
tags:
- Programming
- Machine Learning
- Deep Learning
slug: optimizers-1
---

Happy New Year! This <strike>is going to</strike> was supposed to be a long
one, so sit back and grab a chocolate (and preferably view this on your laptop)

<center>
<iframe src="/articles/2023/res/intro_plot.html" style="width: 100%; height: 650px; border: 0"></iframe>

Some optimization algorithms. Click on a colour in the legend to hide/show it
</center>

# Table of Contents

1. <a href="#introduction">Introduction</a>
    * <a href="#solution-existence">Do Solutions Even Exist?</a>
    * <a href="#structure">How this guide is structured</a>
2. <a href="#gradient-descent-optimizers">Gradient Descent Optimizers</a>
    * <a href="#stochastic-gradient-descent">Stochastic Gradient Descent</a>
    * <a href="#sgd-with-momentum">SGD with Momentum</a>
    * <a href="#sgd-with-nesterov-momentum">SGD with Nesterov Momentum</a>
    * <a href="#gradient-descent-comparision">Putting it all together</a>
3. <a href="#refs-and-footnotes">References and Footnotes</a>
<!--
3. <a href="#adaptive-optimizers">Adaptive Optimizers</a>
    * <a href="#adagrad">AdaGrad</a>
    * <a href="#rmsprop">RMSProp</a>
    * <a href="#rmsprop-with-nesterov-momentum">RMSProp with Nesterov Momentum</a>
    * <a href="#adam">Adam</a>
    * <a href="#nadam-nesterov-adam">NAdam (Nesterov Adam)</a>
    * <a href="#adamw">AdamW</a>
    * <a href="#amsgrad">AMSGrad</a>
    * <a href="#adabound">AdaBound</a>
    * <a href="#adabelief">AdaBelief</a>
4. <a href="#second-order-optimizers">Second Order Optimizers</a>
    * <a href="#newton">Newton</a>
    * <a href="#conjugate-gradients">Conjugate Gradients</a>
        * <a href="#fletcher-reeves">Fletcher-Reeves</a>
        * <a href="#polak-ribiere">Polak-Ribiere</a>
    * <a href="#bfgs">BFGS</a>
    * <a href="#l-bfgs">L-BFGS</a>-->


<h1 id="introduction">Introduction</h1>

Most supervised learning tasks involve optimizing a loss function, in order to
fit the model to the given training data. Of these, the most common is neural
network training: neural networks have millions (even billions) of parameters
which need to be tuned so that the model can predict the right outputs.

Obtaining closed form solutions to neural network problems is more often than
not intractable, and so we perform this optimization algorithmically and 
numerically. The main things we look for in an algorithm that optimizes the
loss function are:

* **It should converge**: Sounds like a no-brainer, but the algorithm should be
  able to decide when and where to stop, and to ensure that the location at 
  which it stops is a local minima.

* **It should converge quickly**: The algorithm should take as few steps as
  possible to converge, as every step requires a parameter update, and updating
  millions (if not billions) of parameters is inefficient. Therefore, it should
  take the optimal steps at every point.

* **It should be able to deal with ambiguity**: Loosely worded, the algorithm 
  would not have the exact value of the gradient: all the algorithms described 
  use a batch of samples to obtain an estimate of the gradient, and the 
  expected value of the gradient obtained should equal the gradient of the 
  function at this point. The algorithm should be able to converge to a local 
  minima even if it obtains incorrect gradients at some steps in the process.

<h2 id="solution-existence">Do solutions even exist?</h2>

We can't really go further without knowing what the loss landscape looks like: 
do solutions even exist? How do we visualize a high-dimensional loss landscape?

A few observations about the loss landscape of a neural network from Goodfellow
are:

1. **As dimensionality of the latent space increases, the probability a
   critical point is a local minima decreases**. The curvature of a point is
   given by the eigenvalues of the hessian: if all the eigenvalues are positive,
   the point is a local minima (and the hessian is positive semi-definite), and
   the opposite for a local maxima. If we consider a random function, choosing 
   the sign of the eigenvalue is akin to tossing a coin. Therefore, in
   n-dimensional space, if we toss n coins to determine these signs, the
   probability that all of them turn up positive is very low. Therefore, high-
   dimensional space has more saddle points than local minima/maxima

2. **There are several equally good local minima**: because of scale invariance,
   if you scale the inputs to a layer down by 10 and multiply the outputs by 10,
   then you get the same resultant network. Also, if you switch the position of
   two neurons in a layer with each other while maintaining the connections, 
   you get the same network. These two similarities result in a large number of
   similar optima, reaching any one of which will optimize the entire network.

Both of these are in our favour, and show us that reaching a local minima in
high-dimensional space should be sufficient to fit the network. We'll now take 
a look at some algorithms which do this.

As for visualizing the loss landscape, this is significantly trickier to do.
This work by [Goldstein et al](https://arxiv.org/pdf/1712.09913v3.pdf) does a
good job of it, but visualizing and comparing the paths taken by optimization 
algorithms on this landscape is very difficult: because what we're seeing is a
projection onto two dimensions, the direction taken by the path need not
correspond to the direction of maximum descent. This repository by [Logan Yang](https://github.com/logancyang/loss-landscape-anim)
had a good implementation of this paper, along with traces of the paths taken
by various optimization algorithms showing why we can't use this to
qualitatively compare different optimization algorithms with each other 

<center>
<img src="/articles/2023/res/loss_landscape_goldstein.png" width=800px></img>

The loss landscape of ResNet-56 (source: Goldstein et al)
</center>

<h2 id="structure">How this guide is structured</h2>

While most deep learning problems use a super high-dimensional loss function, 
for the purposes of this guide we'll use a simple 2-D loss function which is 
a linear combination of gaussians of the following form
$$\begin{gather}
f(x, y) = se^{-(ax+by+c)^2} \\\\
\mathcal{L} = \sum_{i=1}^{n} f_i(x, y)
\end{gather}$$

The good thing about gaussians is that they're easy to differentiate
$$\begin{align}
\frac{\partial f}{\partial x} &= -2a(ax+by+c)f(x,y) \\\\
\frac{\partial f}{\partial y} &= -2b(ax+by+c)f(x,y) \\\\
\frac{\partial^2 f}{\partial x^2} &= -2a^2(1 - 2(ax+by+c)^2)f(x,y) \\\\
\frac{\partial^2 f}{\partial x \partial y} &= -2ab(1 - 2(ax+by+c)^2)f(x,y) \\\\
\frac{\partial^2 f}{\partial y^2} &= -2b^2(1 - 2(ax+by+c)^2)f(x,y)
\end{align}$$

so all the methods can use the exact gradient/hessian of the loss function
rather than a _stochastic_ one. This is kind of cheating, but since this is a
science experiment, let's run with it. about this loss func

$s, a, b, c$ are generated uniform randomly from a suitable range, and I played
around manually with this till I got a loss function that looked funky enough
for my needs. We finally use the following loss function, and it's been
exported to the file `func.dill` if you want to load it in (use dill to load it, 
as there were some errors serializing it via pickle)

<iframe src="/articles/2023/res/loss_fn_interactive.html" style="width: 100%; height: 620px; border: 0"></iframe>

The convergence criterion that's used for all optimizers is when the gradient norm 
is less than 0.05, and all the optimizers are limited to take atmost 1000 steps.

The plots are made in Bokeh/Plotly and are interactive (if you haven't already 
played with the plot we generated in the start). I've done my best to be 
inspired by [Distill](https://distill.pub), most notably [Gabriel Goh](https://distill.pub/2017/momentum/)'s
beautiful, interactive article on momentum.

<h1 id="gradient-descent-optimizers">Gradient Descent Optimizers</h1>

Gradient Descent optimizers converge to a local minimum by simply following the
gradient: there's no adaptiveness here, and it's akin to feeling the area 
around your feet and just taking a small step in the steepest direction, and 
repeating that till you get to the minima. There are a few tricks here and we 
take hints from Physics to speed up the convergence, but most of the algorithm
relies on the gradient, and the speed with which we're already going.

<h2 id="stochastic-gradient-descent">Stochastic Gradient Descent</h2>

SGD is probably the first optimization algorithm one thinks of. It's
deceptively simple: Look around and take a step in the direction where the
gradient decreases the most. Once you've taken the step, **Stop**, look around
again, and repeat until you're at the minima (the gradient is sufficiently 
small or you come back to a point you've visited).

Th *S* in SGD comes from the fact that the gradient that the algorithm obtains
in practice is not perfect: it's an approximation of the actual gradient of the
loss function, based on the batch of examples that are sampled. However, this
approximates the gradient reasonably well, and in the long run, the expected
path taken by this algorithm comes out to be the same as the path taken when we
can perfectly obtain the gradient.

The update rule for SGD is fairly simple:

$$\begin{align}
\theta_{t+1} &\leftarrow \theta_{t} - \epsilon g(\theta_{t})
\end{align}$$

Combining this with a convergence criterion gives us the algorithm (implemented
in python here)

```python
def SGD(L, G, p0, eps=5e-2):
    p = p0
    g = np.inf
    while norm(g) > 5e-2:
        g = G(p)
        p = p - eps*g
```

<h2 id="sgd-with-momentum">SGD with Momentum</h2>

While SGD is simple, it is slow to converge, taking several more steps than
required. This is because we come to a stop once we take a step, and the size
of the next step is solely determined by the gradient at that point. This means
that if we're in a long stretch where the gradient is small, we can only 
descend at the speed $\epsilon g$, even though we know that the stretch is
reasonably long. This slows down our algorithm and makes it take a longer time
to converge.

Momentum counters this by providing some inertia to the process. Intuitively,
if SGD is a person stopping and taking a step in the direction of maximum 
descent, momentum is equivalent to throwing a ball down the incline of a given
mass and seeing where it settles. If you take a look at the path momentum
follows in the introduction plot, you can see that it doesn't immediately stop
when it comes to a point with a zero (or very small) gradient; instead, it
oscillates until it loses all it's velocity.

How do we simulate adding 'mass' to the update steps? We claim that the ball
moves at a velocity $v$, and model $v$ as an exponential moving average of the
current velocity and the gradient at the current point. The update equations
are as follows:

$$\begin{align}
v_{t+1} &\leftarrow \alpha v_{t} - \epsilon g(\theta_{t}) \\\\
\theta_{t+1} &\leftarrow \theta_{t} + v_{t+1}
\end{align}$$

What's the maximum velocity we can move at? If all the gradients are in the
same direction for an infinite (practically a very large) period of time, then
this velocity is equal to

$$v_{\text{max}} = \frac{\epsilon g}{1-\alpha}$$

This can be derived by expanding out the recurrence in the update step, to
obtain an infinite GP. This GP converges when $\alpha < 1$ to $1/(1-\alpha)$.
We can think of $1-\alpha$ as the 'mass' of the ball: the smaller this quantity
is, the faster the ball will move.

Generally (and in this simulation as well), $\alpha = 0.9$, so $1-\alpha = 0.1$.
This means that we can move atmost ten times faster than the step size at a
point, and this is what causes momentum to converge faster!

```python
def SGD_momentum(L, G, p0, v0=0, eps=5e-2, a=0.9):
    p = p0
    v = v0
    g = np.inf
    while norm(g) > 5e-2:
        g = G(p)
        v = a*v - eps*g
        p = p + v
```

What do these gradient updates look like in practice? For starters, all changes
in the direction of the path are caused due to changes in the gradient. Where
the path takes a turn, the gradient is normal or antiparallel to the current
velocity, and at places where the path is straight, both the gradient and the
velocity are parallel. We can draw out the update vectors at two points in the
path above to see how this works.

<iframe src="/articles/2023/res/momentum_vectors.html" style="width: 100%; height: 650px; border: 0"></iframe>

<h2 id="sgd-with-nesterov-momentum">SGD with Nesterov Momentum</h2>

If you've seen the path that momentum takes, there is one issue: _Momentum
doesn't stop very soon_. It's easy to get the ball rolling, but harder to stop
it. This happens because the gradient that's added to the path is the gradient
_at the current point_, not the gradient _at the point at which we would have 
been, if we took the step_. In a continuous, real-world scenario, this 
difference is infinitesimal, but in a numerical scenario, it becomes 
significant if our step size is not small enough. This is also not an issue if 
our gradients at consecutive points are similar, but becomes an issue if we
'jump' across a local minima: momentum would push us even further forward, 
because the gradient at the current point is downward. 

This 'bug' was discovered by Nesterov, and the fix was to compute the gradient
at $\theta_{t} + \alpha v_{t}$ (the position we will be at, if the gradient is 
zero) rather than at $\theta_{t}$ (our current position). This 'pulls' the
gradient back if we jump across a minima

<iframe src="/articles/2023/res/nesterov_comparision.html" style="width: 100%; height: 650px; border: 0"></iframe>

The implementation and update are quite similar, with just a minor update to
the gradient calculation.

$$\begin{align}
v_{t+1} &\leftarrow \alpha v_{t} - \epsilon g(\theta_{t} + \alpha v_{t}) \\\\
\theta_{t+1} &\leftarrow \theta_{t} + v_{t+1}
\end{align}$$

```python
def SGD_nesterov(L, G, p0, v0=0, eps=1e-2, a=0.9):
    p = p0
    v = v0
    g = np.inf
    while norm(g) > 5e-2:
        g = G(p + a*v)
        v = a*v - eps*g
        p = p + v
```

<h2 id="gradient-descent-comparision">Putting it all together</h2>

Here's an interactive demo, showing the paths taken by SGD, SGD with Momentum
and SGD with Nesterov Updates. The arrows have the same colour scheme as
before, and show the directions in which the path is pulled (their sum is the
next resultant step). Playing around with this should give you an idea of how
these algorithms update themselves

<iframe src="/articles/2023/res/comparision_plot.html" style="width: 100%; height: 650px; border: 0"></iframe>

Even though there are a large number of new algorithms for optimization, SGD
with Nesterov momentum (along with Adam) remains the algorithm of choice for
training very large neural networks: it's stable, explainable and converges
nicely.

<!--
<h2 id="adaptive-optimizers">Adaptive Optimizers</h2>


<h2 id="adagrad">AdaGrad</h2>

$$\begin{align}
r_{t+1} &\leftarrow r_{t} + (g(\theta_{t}))^2 \\\\
v_{t+1} &\leftarrow -\frac{\epsilon g(\theta_{t})}{\sqrt{r_{t+1} + \delta}} \\\\
\theta_{t+1} &\leftarrow \theta_{t} + v_{t+1}
\end{align}$$

```python
def AdaGrad(L, G, p0, eps=5e-2):
    r = np.zeros(2)
    p = p0
    v = 0
    g = np.inf
    while norm(g) > 5e-2:
        g = G(p)
        r = r + g**2
        v = - ((eps)/np.sqrt(r))*g
        p = p + v
```

<h2 id="rmsprop">RMSProp</h2>

$$\begin{align}
r_{t+1} &\leftarrow \rho r_{t} + (1-\rho)(g(\theta_{t}))^2 \\\\
v_{t+1} &\leftarrow -\frac{\epsilon g(\theta_{t})}{\sqrt{r_{t+1} + \delta}} \\\\
\theta_{t+1} &\leftarrow \theta_{t} + v_{t+1}
\end{align}$$

```python
def RMSProp(L, G, p0, eps=1e-2, decay=0.9):
    r = np.zeros(2)
    p = p0
    v = 0
    g = np.inf
    while norm(g) > 5e-2:
        g = G(p)
        r = decay*r + (1-decay)*g**2
        v = - ((eps)/np.sqrt(r+1e-7))*g
        p = p + v
```

<h2 id="rmsprop-with-nesterov-momentum">RMSProp with Nesterov Momentum</h2>

$$\begin{align}
r_{t+1} &\leftarrow \rho r_{t} + (1-\rho)(g(\theta_{t} + \alpha v_{t}))^2 \\\\
v_{t+1} &\leftarrow \alpha v_{t} - \frac{\epsilon g(\theta_{t})}{\sqrt{r_{t+1} + \delta}} \\\\
\theta_{t+1} &\leftarrow \theta_{t} + v_{t+1}
\end{align}$$

```python
def RMSProp_nesterov(L, G, p0, eps=1e-2, decay=0.9, a=0.9):
    r = np.zeros(2)
    p = p0
    v = 0
    g = np.inf
    while norm(g) > 5e-2:
        g = G(p + a*v)
        r = decay*r + (1-decay)*g**2
        v = a*v - ((eps)/np.sqrt(r+1e-7))*g
        p = p + v
```

<h2 id="adam">Adam</h2>

```python
def Adam(L, G, p0, eps=1e-3, b1=0.9, b2=0.999):
    r = np.zeros(2)
    s = np.zeros(2)
    p = p0
    v = 0
    g = np.inf
    t = 0
    while norm(g) > 5e-2:
        g = G(p)
        t += 1
        s = b1*s + (1-b1)*g
        r = b2*r + (1-b2)*g**2
        sh = s/(1-b1**t)
        rh = r/(1-b2**t)
        v = - ((eps)/np.sqrt(rh+1e-7))*sh
        p = p + v
```

<h2 id="nadam-nesterov-adam">NAdam (Nesterov Adam)</h2>

```python
def NAdam(L, G, p0, eps=1e-3, b1=0.9, b2=0.999):
    r = np.zeros(2)
    s = np.zeros(2)
    p = p0
    v = 0
    g = np.inf
    t = 0
    while norm(g) > 5e-2:
        g = G(p)
        t += 1
        s = b1*s + (1-b1)*g
        r = b2*r + (1-b2)*g**2
        sh = b1*s/(1-b1**t) + (1-b1)*g/(1-b1**t) # nesterov step
        rh = r/(1-b2**t)
        v = - ((eps)/np.sqrt(rh+1e-7))*sh
        p = p + v
```

<h2 id="adamw">AdamW</h2>

```python
def AdamW(L, G, p0, eps=1e-3, b1=0.9, b2=0.999, l=1):
    r = np.zeros(2)
    s = np.zeros(2)
    p = p0
    v = 0
    g = np.inf
    t = 0
    while norm(g) > 5e-2:
        g = G(p)
        t += 1
        s = b1*s + (1-b1)*g
        r = b2*r + (1-b2)*g**2
        sh = s/(1-b1**t)
        rh = r/(1-b2**t)
        v = - ( ((eps)/np.sqrt(rh+1e-7))*sh + l*p ) # adamW step
        p = p + v
```

<h2 id="amsgrad">AMSGrad</h2>


<h2 id="adabound">AdaBound</h2>


<h2 id="adabelief">AdaBelief</h2>


<h1 id="second-order-optimizers">Second Order Optimizers</h1>


<h2 id="newton">Newton</h2>


<h2 id="conjugate-gradients">Conjugate Gradients</h2>


<h3 id="fletcher-reeves">Fletcher-Reeves</h3>


<h3 id="polak-ribiere">Polak-Ribiere</h3>


<h2 id="bfgs">BFGS</h2>


<h2 id="l-bfgs">L-BFGS</h2>-->


<h1 id="refs-and-footnotes">References and Footnotes</h1>

1. Goh, "Why Momentum Really Works", Distill, 2017. 
   [http://doi.org/10.23915/distill.00006](http://doi.org/10.23915/distill.00006)
2. Goodfellow, Ian, Bengio, Yoshua and Courville, Aaron. Deep Learning. : MIT 
   Press, 2016. 
3. Melville, James. Nesterov Accelerated Gradient and Momentum. 
   [https://jlmelville.github.io/mize/nesterov.html](https://jlmelville.github.io/mize/nesterov.html)

---

This was supposed to also feature adaptive optimizers (AMSGrad, RMSProp, Adam 
and friends), but due to CCIC happening in the last week of December, I didn't
get the time to do this properly, and the second semester starts <strike>in a
couple days</strike> tomorrow, so hard deadline :/ I'll try to get part 2 out
as soon as possible, but it might be a while. In the meantime, exploring the
source might help for the impatient.

For the complete code, and to play around and implement your own optimizers, 
check out the repository here

<center>
<a href="https://github.com/Aniruddha-Deb/optimizers"><img src="https://gh-card.dev/repos/Aniruddha-Deb/optimizers.svg"></a>
</center>
