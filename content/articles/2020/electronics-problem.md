Title: An Interesting Electronics Problem
Date: 2020-04-29 22:20
Category: Electronics
Slug: interesting-electronics-problem


An interesting electronics problem I encountered recently was this: Find the resistance between points A and B in the following resistor network

![resistor network]({static}res/iep_1.png)

This looks like a simple wheatstone bridge problem, but note that the top right and bottom left resistances are R and not r. To solve this problem, we'll use the concept of symmetry and a few tricks. Let's start by connecting a battery to the circuit and labeling the currents and loops

![tweaked resistor network]({static}res/iep_2.png)

We notice that there is no mixing of currents in node B. This allows us to disconnect the node and separate it into two components, both of which are relatively easy to solve.

![currents]({static}res/iep_3.png)

The net resistance is now $$\frac 1 {R\_{n}} = \frac 1r + \frac 1 {R\_p} \tag{1}$$, where \\( R\_p \\) is the resistance of the disconnected network. This resistance can be easily found by using KVL and KCL after connecting a battery to the network.

![loops]({static}res/iep_4.png)

Solving the loops gives us the equations
$$\begin{align} & V = Ri\_3 + ri\_1 \tag{2} \\\\ & 2ri\_1 - ri\_3 = Ri\_3 \tag{3} \end{align}$$
Solving these gives us $$V = \frac{3Rr + r^2}{R+r}i\_1$$
The net current through the cell is \\( i = i\_1 + i\_3 = \frac{R+3r}{R+r}i\_1 \\). Therefore, the net resistance \\(R\_p = \frac Vi = \frac{r(3R+r)}{3r+R} \\)
We can now get \\(R\_n\\) by substituting \\( R\_p \\) in equation \\( (1) \\) 
$$\begin{gather}\frac 1 {R\_n} = \frac 1r + \frac {3r+R}{r(3R+r)} \\\\ 
\boxed{R\_n = \frac{r(3R+r)}{4(R+r)}}\end{gather}$$ 
-------------------
<sup>p.s: The `\eqref` or `\ref` commands don't work for some reason. I'll have to figure out why.</sup>
