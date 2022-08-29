Title: Variance Estimation in Heteroscedastic Regression
Date: 2022-08-29 18:00
Category: Programming
Tags: Programming, Machine Learning
Slug: heteroscedastic-variance-estimation
Summary: Most of the times, the regression models we need to fit don't have a constant standard deviation, but rather one that is some function of $x$. In this article, I try to learn a model with variance varying linearly as a function of x: kind of like a _regression on variance_

## Motivation

Most linear regression models assume 

$$y^{i} \approx \mathcal{N}(\theta^T x^{i}, \sigma^2)$$

The standard closed form for this, obtained via finding the MLE estimate, gives $(X^T X)^{-1} X^T Y$, where $X$ is the example matrix of shape $(m,n)$ and $Y$ is the label vector of shape $(n,1)$. Note that $m$ is the number of training examples and $n$ is the number of features.

However, the variance need not always be constant. Consider a model where the variance is varying linearly (or rather just increasing) with $x$: an example would be the [House prices dataset](https://www.kaggle.com/code/chanakyavivekkapoor/house-price-prediction)

![img](res/house_prices.png)

While there are feature transformations that would make this less heteroscedastic, this article focuses on learning the variance parameters, so along with our regression estimate, we can provide a variance estimate as well

## The Model

We assume that the **standard deviation** (not variance) is a linear function of $x$

$$y^{i} \approx \mathcal{N}(\theta_m^T x^{i}, (\theta_v^T x^{i})^2)$$

The log-likelihood function is hence

$$\mathcal{LL}(\theta_m, \theta_v) = -\frac{m}{2} \log 2\pi - \sum_{i=1}^m \log \theta_v^T x^{i} - \frac{1}{2} \sum_{i=1}^m \frac{(y^{i} - \theta_m^T x^{i})^2}{(\theta_v^T x^{i})^2}$$

Differentiating with respect to $\theta_v$ gives us the gradient for $\theta_v$:

$$\frac{\partial \mathcal{LL}}{\partial \theta_v} = - \sum_{i=1}^m \frac{x^{i}}{\theta_v^T x^{i}} + \sum_{i=1}^m x^{i} \frac{(y^{i} - \theta_m^T x^{i})^2}{(\theta_v^T x^{i})^3}$$

Rearranging this gives us, in a matrix form,

$$\frac{\partial \mathcal{LL}}{\partial \theta_v}= X^T \left( \frac{E^2 - S^2}{S^3} \right)$$

Where $X$ is our example matrix, $E$ is the sum of squared error vector and $S$ is the standard deviation vector. This is a nice, concise form that we can use in our code. However, because of the $V$ term in the denominator, **I couldn't obtain a closed form for this, and had to do gradient descent on the parameters**. Even getting into second derivative methods was getting a bit tedious. If you do find a closed form, let me know :)

The derivative with respect to $\theta_m$ is pretty standard: we get

$$\frac{\partial \mathcal{LL}}{\partial \theta_m} = \sum_{i=1}^m x^{i} \frac{(y^{i} - \theta_m^T x^{i})}{(\theta_v^T x^{i})^2}$$

## An Implementation

Implementation was fairly straightforward, using gradient descent:

```python
def LL(X,Y,T_mean,T_std):
    S = (X@T_std)
    M = (X@T_mean)
    return -(((Y-M)**2)/(2*S**2) + np.log(S)).mean()

def grad_LL_var(X,Y,T_mean,T_std):
    S = (X@T_std)
    M = (X@T_mean)
    return X.T@(((Y-M)**2 - S**2)/(S**3))

def grad_LL_mean(X,Y,T_mean,T_std):
    S = (X@T_std)
    M = (X@T_mean)
    return X.T@((Y-M)/(S**2))

def grad_desc(X,Y,T_mean,T_std,eta_mean=0.001,eta_std=0.001,n_iter=100000,conv_mean=0.01,conv_std=0.01):
    
    i = 0
    new_T_mean = T_mean
    new_T_std = T_std
    while i < n_iter:
        new_T_mean = T_mean + eta_mean*grad_LL_mean(X,Y,T_mean,T_std)
        new_T_std = T_std + eta_std*grad_LL_var(X,Y,T_mean,T_std)
        
        if ((np.abs(new_T_mean-T_mean)).max() < conv_mean and (np.abs(new_T_std-T_std)).max() < conv_std):
            break
            
        T_mean = new_T_mean
        T_std = new_T_std
        
        i += 1
        
    print(f"Converged in {i} steps")
    
    return (new_T_mean, np.abs(new_T_std)) # if we don't take abs, this can give negative values (which we should ignore)
```

And this converged nicely to some generated data

![hetero_model](res/hetero_sd_model.png)
