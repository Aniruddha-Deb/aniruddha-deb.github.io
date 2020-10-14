Title: Math Notes: Lagrange interpolation
Date: 2020-08-14 17:37
Category: Mathematics
Tags: Mathematics, Math Notes
Slug: math-notes-1

This is a small set of posts that come into the category of "notes": 
self-explanations of concepts that I have recently picked up and found 
interesting.

## Lagrange Interpolation

[Lagrange Interpolation][1] is a concept that allows us to find a polynomial of 
least degree passing through a given set of points. Specifically:

> If $S = \{(x\_i, y\_i) : x\_i, y\_i \in R, 1 \lt i \le n\}$, then the polynomial
> of least degree passing through all the points in $S$ is given by
> $$P(x) = \sum\_{i=1}^n L\_i(x) \cdot y\_i$$
> where $$L\_i(x) = \frac{(x-x\_1)(x-x\_2)...(x-x\_{i-1})(x-x\_{i+1})...(x-x\_n)}
{(x\_i-x\_1)(x\_i-x\_2)...(x\_i-x\_{i-1})(x\_i-x\_{i+1})...(x\_i-x\_n)}$$
> or simply,
> $$P(x) = \sum\_{i=1}^n \frac{\prod\_{r \ne i}(x-x\_r)}{\prod\_{r \ne i}{(x\_i-x\_r)}} \cdot y\_i$$
> note that the degree of polynomial $P < n$.

Here's an example:

> If $P(x)$ is a function such that $P(-1) = -2,  P(0) = 2, P(1) = 0, P(2) = 2$, 
> then find $P(x)$

So we have $S = {(-1,-2), (0,2), (1,0), (2,2)}$. Using lagrange interpolation 
gives us $P(x)$ as:
$$\begin{gather}
P(x) = \frac{(x-0)(x-1)(x-2)}{(-1-0)(-1-1)(-1-2)} \cdot -2 + \\\\
\frac{(x+1)(x-1)(x-2)}{(0+1)(0-1)(0-2)} \cdot 2 + \\\\
\frac{(x+1)(x-0)(x-2)}{(1+1)(1-0)(1-2)} \cdot 0 + \\\\
\frac{(x+1)(x-0)(x-1)}{(2+1)(2-0)(2-1)} \cdot -2
\end{gather}$$
or, once simplified,
$$P(x) = x^3 - 3x + 2$$

This technique is also useful for other stuff, such as finding patterns in 
hard-to-decipher sequences:

> Find the nth term of the sequence $$5, 65, 325, 1025, 2501 ...$$

Letting $T(1) = 5, T(2) = 65$ and so on, lagrange interpolation gives us:
$$\begin{gather}
T(n) = \frac{5(x-2)(x-3)(x-4)(x-5)}{(-1)(-2)(-3)(-4)} + \\\\ 
\frac{65(x-1)(x-3)(x-4)(x-5)}{(1)(-1)(-2)(-3)} + \\\\
\frac{325(x-1)(x-2)(x-4)(x-5)}{(2)(1)(-1)(-2)} + \\\\
\frac{1025(x-1)(x-2)(x-3)(x-5)}{(3)(2)(1)(-1)} + \\\\
\frac{2501(x-1)(x-2)(x-3)(x-4)}{(4)(3)(2)(1)}
\end{gather}$$
simplified:
$$T(n) = 4n^4 + 1$$

Of course, there are some problems that cannot be solved by this technique, 
namely problems where it is specified that the polynomial is of a higher order
than the number of points it passes through:
> Let $P(x)=x^4+ax^3+bx^2+cx+d$. If $P(1) = 1, P(2)=8, P(3)=27, P(4)=64$, then 
  the value of $P(5)$ is?

The lagrange interpolated polynomial for the above values is $P(x) = x^3$. However, 
this gives the wrong answer of $P(5) = 145$. The correct answer is $P(5) = 149$, 
because we have been asked to fit a polynomial of higher order in this equation.

Also, this technique should only be used as a last resort for pattern finding. 
This is extremely computation heavy and is more of a bruteforce algorithm, that 
is better suited to computers rather than manual calculation. Most math softwares
have a lagrange interpolation function in them. Geogebra's is called `Polynomial()`.

As a bonus, here's the code I used to generate the above function:
```python
import sys

pts = []
for i in range(1,len(sys.argv),2):
	pts.append([int(sys.argv[i]), int(sys.argv[i+1])])

output = "P(x) = "

for i in pts:
	nr = ""
	dr = ""
	for r in pts:
		if r is i:
			continue
		dr += "({})".format(i[0]-r[0])
		if r[0] < 0:
			nr += "(x+{})".format(-r[0])
		else:
			nr += "(x-{})".format(r[0])
	output += "\\frac{{{2}{0}}}{{{1}}} + ".format(nr,dr,i[1])

print(output)
```


 [1]: https://en.wikipedia.org/wiki/Lagrange_multiplier

