---
title: Icosahedron Resistor Network
publishDate: '2020-06-09T12:30:00'
categories: Electronics
tags:
- Physics
- Electronics
slug: icosahedron-resistor-network
---

> Consider the icosahedral resistance network shown in the following figure. Each edge is made of a rod of resistance $r$. Select the option(s) that is(are) correct:<br>
> ![icosahedron](/articles/2020/res/icosa_res_net/icosa_1.png)
> A) The resistance between points A and B is $\frac{r}{2}$<br>
> B) The resistance between points A and B is $\frac{r}{3}$<br>
> C) The resistance between any two adjacent vertices is $\frac{11r}{30}$<br>
> D) The resistance between any two adjacent vertices is $\frac{11r}{20}$<br>

This question looks really tricky. This is a variation of the problem of finding the resistance of a wire cube. This can be solved in a similar way, using symmetry and equipotential reduction.

Let's start off by finding the resistance between A and B, since this is easier than finding the resistance between adjacent vertices. On connecting a battery, the points marked in the same colour will be at the same potential.

![battery](/articles/2020/res/icosa_res_net/icosa_2.png)

You can clearly see the symmetry now. If we connect all the points with the same potential, we end up with the following resistor network (each resistance is $r$).

![res net](/articles/2020/res/icosa_res_net/res_net.png)

This is simple to solve. It's resistance is
$$R\_{AB} = \frac r5 + \frac r{10} + \frac r5 = \boxed{\frac r2}$$
which corresponds to option (A).

Solving the network between adjacent vertices is a lot trickier. The first trick is to pick a pair of vertices from which symmetry is easily identifiable. If I connect my battery as shown in the following figure, it is easy to identify which points are equipotential and how the currents are flowing.

![currents](/articles/2020/res/icosa_res_net/icosa_3.png)

The dotted line shows the plane of symmetry of this icosahedron perpendicular to $CD$ whereas the blue dots show equipotential nodes. We can see that no current flows through $R\_{AJ}$ and $R\_{EB}$ since the ends are at the same potential. Also, at all equipotential points, no mixing of currents occurs. This means that $I\_{AC} = I\_{AD}$ and $I\_{CE} = I\_{ED}$, along with a few others. Performing some modifications on this circuit in line with the above observations reduces the complexity quite drastically as shown below:

![simple](/articles/2020/res/icosa_res_net/icosa_4.png)

Simplifying these resistors, we obtain a cubical network with a resistor across two opposite face diagonals

![cube](/articles/2020/res/icosa_res_net/icosa_5.png)

It is easy to see that $V\_F = V\_L$ and $V\_G = V\_K$. Connecting these two points and getting rid of the resistances $R\_{GK}$ and $R\_{LF}$, we get the following resistor network:

![simplest](/articles/2020/res/icosa_res_net/icosa_6.png)

It is now simple to calculate the resistance across CD by using the formulae for resistors in parallel and series.

$$\begin{gather} 
\frac 1 {R\_{FG}} = \frac 2 r + \frac 2 {3r} \\\\
R\_{FG} = \frac{3r}{8} \\\\
\frac{1}{R\_{CD}} = \frac{8}{11r} + \frac{2}{r} \\\\
\boxed{R\_{CD} = \frac{11r}{30}} 
\end{gather}$$

Which corresponds to option (C)

A good problem that I came up with on my own; the next step is to do the same for a dodecahedric resistor network. Stay tuned for that :)
