Title: Optimizers
Date: 2023-01-01 15:00
Category: Programming
Tags: Programming, Machine Learning
Slug: optimizers
Status: draft

Happy New Year! This is going to be a long one, so sit back and grab a 
chocolate (and preferably view this on your laptop)

<iframe src="/articles/2023/res/optim_intro.html" style="width: 100%; height: 650px; border: 0"></iframe>

# Table of Contents

1. <a href="#introduction">Introduction</a>
    * <a href="#solution-existence">Do Solutions Even Exist?</a>
    * <a href="#structure">How this guide is structured</a>
2. <a href="#gradient-descent-optimizers">Gradient Descent Optimizers</a>
    * <a href="#stochastic-gradient-descent">Stochastic Gradient Descent</a>
    * <a href="#sgd-with-momentum">SGD with Momentum</a>
    * <a href="#sgd-with-nesterov-momentum">SGD with Nesterov Momentum</a>
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
    * <a href="#l-bfgs">L-BFGS</a>
5. <a href="#refs-and-footnotes">References and Footnotes</a>


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
repeating that till you get to the minima

<h2 id="stochastic-gradient-descent">Stochastic Gradient Descent</h2>

$$\begin{align}
\theta_{t+1} &\leftarrow \theta_{t} - \epsilon g(\theta_{t})
\end{align}$$

```python
def SGD(L, G, p0, eps=1e-2):
    p = p0
    g = np.inf
    while norm(g) > 5e-2:
        g = G(p)
        p = p - eps*g
```

<h2 id="sgd-with-momentum">SGD with Momentum</h2>

$$\begin{align}
v_{t+1} &\leftarrow \alpha v_{t} - \epsilon g(\theta_{t}) \\\\
\theta_{t+1} &\leftarrow \theta_{t} + v_{t+1}
\end{align}$$

```python
def SGD_momentum(L, G, p0, v0=0, eps=1e-2, a=0.9):
    p = p0
    v = v0
    g = np.inf
    while norm(g) > 5e-2:
        g = G(p)
        v = a*v - eps*g
        p = p + v
```

<h2 id="sgd-with-nesterov-momentum">SGD with Nesterov Momentum</h2>

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

<h2 id="adaptive-optimizers">Adaptive Optimizers</h2>


<h2 id="adagrad">AdaGrad</h2>

$$\begin{align}
r_{t+1} &\leftarrow r_{t} + (g(\theta_{t}))^2 \\\\
v_{t+1} &\leftarrow -\frac{\epsilon g(\theta_{t})}{\sqrt{r_{t+1} + \delta}} \\\\
\theta_{t+1} &\leftarrow \theta_{t} + v_{t+1}
\end{align}$$

```python
def AdaGrad(L, G, p0, eps=1e-2):
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


<h2 id="l-bfgs">L-BFGS</h2>


<h1 id="refs-and-footnotes">References and Footnotes</h1>


---

<sup id="footnote-1">1</sup>
