Title: HackerFX v2
Date: 2022-12-08 01:00
Category: Programming
Tags: Programming
Slug: hackerfx-v2

Some of you might have come across [HackerFX](https://github.com/Aniruddha-Deb/HackerFX),
an image binarizer. This was written a long time back, when the only language I 
knew was Java, and when I was still in school. 

An update was on the cards for a while, because I wanted to change my desktop 
background (which still looks surprisingly pretty for something made so long 
ago). I started playing around with PIL today evening to update this, and the 
end result is [HackerFX v2](https://github.com/Aniruddha-Deb/hackerfx-v2), a 
python rewrite that supports multicoloured input images, hex, file dumps, 
variable colors and a manual 5x5 font for the output charactes (so the aspect 
ratio doesn't have to be manually tweaked). It's a step jump in every way, and 
the images it generates are super pretty

![jojo](res/jojo.jpg)
![jojo_out](res/jojo_out.png)

Especially with hi-res shots, you have to zoom in to tell the difference. The 
performance is also very cool, given that you're iterating over millions of 
pixels. This does it all in less than 10 seconds.

![input](res/hallway.jpeg)
![output](res/hallway_out.png)

More examples are there in the github repo, and I haven't played around with 
the options much to generate prettier ones (it's getting kind of late, should sleep).
Feel free to clone the code, give it a spin on your images and enter the matrix :)
