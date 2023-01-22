Title: L2 regularization intuition
Date: 2023-01-22 10:15
Category: Mathematics
Tags: Mathematics, Machine Learning, Deep Learning
Slug: l2-regularization

A nice intuition for L2 regularization comes from having a prior on the
distribution of parameters: the prior assumes that the parameters are close to
zero. Let's assume that the prior is $\mathcal{N}(0, \Sigma)$. The MAP estimate
of the parameters would then be

$$\begin{align}
\theta_{\text{MAP}} &= \text{argmax}\_{\theta} \; P(\theta | D) \\\\
    &= \text{argmax}\_{\theta} \; P(D | \theta) P(\theta) \\\\
    &= \text{argmax}\_{\theta} \; \log P(D | \theta) + \log P(\theta)
\end{align}$$

$\log P(D | \theta)$ is simply the log-likelihood of the model, and optimizing
that would give you the MLE parameters. However, incorporating $\log P(\theta)$
gives us the L2 regularization parameter

$$\log P(\theta) = -\log((2\pi)^{n/2}|\Sigma|^{1/2}) - \frac{\theta^T \Sigma^{-1} \theta}{2}$$

The constant at the start goes out of the argmax, and we're left with the L2
regularization term. Taking a negative on both sides would give us the 
negative log-likelihood, which is the unregularized loss function. We'd then
minimize $\theta$. The net expression would look something like this:

$$\theta_{\text{MAP}} = \text{argmin}\_{\theta} \; - P(\theta | D) + \frac{1}{2} \theta^T \Sigma^{-1} \theta$$

Regularization generally features a strength term $\lambda$: We can think of
$\lambda$ as being the inverse of every term in the diagonal of the covariance 
matrix (if it is a diagonal covariance matrix). We'd then get

$$\theta_{\text{MAP}} = \text{argmin}\_{\theta} \; - P(\theta | D) + \frac{1}{2} \lambda\theta^T\theta$$

And this is the familiar L2 reglarized loss function.

-----

I got this from one of the [Deep
Learning](https://www.cse.iitd.ac.in/~parags/teaching/col775/) lectures; it's a
nice treatment which I couldn't find in other places (maybe because I haven't
looked hard enough). Goodfellow certainly doesn't feature it though.


