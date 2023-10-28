---
title: Electronic Clock II - Generating the Clock Signal pt. 2
publishDate: '2018-06-16T10:30:00'
slug: electronic-clock-2-ii
categories: Electronics
---

In the previous post, we saw how to make a 2Hz clock signal. However, for the seconds counter, we will need a 1Hz clock signal. In order to achieve this, I will clock down the frequency using a JK Flip Flop:

### Flip-Flop: Concept
A Flip flop is a one-bit storage device which looks somewhat like this:

![flip flop](/articles/2018/res/flip_flop.png)

The truth table of this device looks somewhat like this:

![truth table](/articles/2018/res/jk-flip-flop-truth-table.jpg)

Note that the flip flop toggles only on the rising edge of the clock. Therefore, in order to clock down the frequency by 2, we need to set the J and K bits high and feed the clock signal in to the CLK pin, thereby obtaining a 1Hz signal on the Q pin. 

### Adding the flip-flop to our circuit:
On adding the flip flop to our circuit, the schematic looks somewhat like this (The 4060 has been carried over from the previous post):

![1hz schematic](/articles/2018/res/1hz_schematic.png)

As calculated, this gives us a frequency of 1 Hz on the Q pin

![oscilloscope output](/articles/2018/res/pic.png)

This concludes our clock signal source. In the next post, we will have a look at counting seconds with the clock signal. 

\- Deb
