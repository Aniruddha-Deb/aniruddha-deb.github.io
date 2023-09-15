---
title: Solving the African Integral (from YG file cover)
publishDate: '2020-07-09T20:30:00'
categories: Mathematics
tags:
- Mathematics
slug: african-integral
---

A long time ago, I gave my friend (Let's call him C) an integral to solve. He came back to me a few days later and the conversation went something like this:

> **C:** Debu, I couldn't solve that African integral you gave me.<br>
> **Me:** Ok, but why are you calling it African?<br>
> **C:** Because Africa is a really big continent, y'know?<br>
> **Me:** Ok, but isn't Asia bigger?<br>
> **C:** Debu, please stop making me feel dumb<br>

 The integral in question appears prominently on the YG file cover as well, and is also featured in Advanced Problems in Mathematics for JEE(A) by Vikas Gupta (Question 24 chapter 7, for those following along)

![YG File cover](/articles/2020/res/yg_file.jpg)

> Evaluate $$\int e^{x\sin x + \cos x} \left( \frac{x^4\cos^3x - x\sin x + \cos x}{x^2 \cos^2x}\right) dx$$

 This looks fearsome, but we can solve it easily by extending the trick $\int e^x (f(x) + f'(x)) dx = e^xf(x) + c$ just a little bit. Consider the function $$e^{g(x)}f(x)$$ Differentiating said function, we see that $$\frac{d}{dx} (e^{g(x)}f(x)) = e^{g(x)}(f'(x) + g'(x)f(x))$$ Rearranging the terms and integrating on both sides: $$e^{g(x)}f(x) = \int e^{g(x)}(f'(x) + g'(x)f(x)) dx$$ For the given problem, $g(x) = x\sin x + \cos x \implies g'(x) = x\cos x$. Therefore, the answer will be something of the form $$I = e^{x\sin x + \cos x} f(x) + c$$ The problem now becomes finding $f(x)$, which we can do through some rearrangement. Rewriting the problem to fit in $g'(x)$, the problem becomes: $$I = \int e^{x\sin x + \cos x} \left( x\cos x \cdot x + \frac{\sec x}{x^2} - \frac{\tan x \sec x}{x}\right) dx$$ We can see that the first term in the bracket implies that $f(x) = x$, but $f'(x) \ne \frac{\sec x}{x^2} - \frac{\tan x \sec x}{x}$. It's easy to see that the last two terms have some kind of pattern going on, as $\frac{d}{dx}\sec x = \sec x \tan x$ and $\frac{d}{dx} \frac{1}{x} = -\frac{1}{x^2}$. The last two terms can be rewritten as $\frac{d}{dx} \left( \frac{\sec x}{x}\right)$. Go through the above steps once again if you're unsure of what is happening, because this is important. The integral can then be rewritten as: 
$$I = \int e^{x\sin x + \cos x} \left( x\cos x \cdot x - \frac{d}{dx} \left( \frac{\sec x}{x}\right) \right) dx$$

We're finally getting somewhere! We had initially assumed that $f(x) = x$, but now, seeing the differential term in the bracket, let's assume 
$$f(x) = x - \frac{\sec x}{x} \implies f'(x) = 1 - \frac{d}{dx} \left( \frac{\sec x}{x}\right)$$

Also, $g'(x)f(x)$ then becomes 
$$g'(x)f(x) = x\cos x \left(x - \frac{\sec x}{x}\right) = x\cos x \cdot x - 1$$

Adding them together, we get
$$g'(x)f(x) + f'(x) = x\cos x \cdot x - \frac{d}{dx} \left( \frac{\sec x}{x}\right)$$

Which is the term in the brackets in the integral. Thus, $f(x) = x - \frac{\sec x}{x}$. We have now solved our integral, and the answer is
$$\boxed{I =  e^{x\sin x + \cos x} \left( x - \frac{\sec x}{x}\right) + c}$$
