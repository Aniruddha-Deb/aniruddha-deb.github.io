---
title: Python Crash Course
publishDate: '2017-12-22T10:30:00'
categories: Programming
slug: python-crash-course
summary: My initial experience with learning Python and using it to create a GTD app
draft: true
---

Recently, I felt the need of creating a to-do app based on the getting things done principle (link here). I had been using MyLifeOrganized in a virtual machine on my mac, but it just wasn't cutting it. Things 3 and OmniFocus for Mac were too pricey and other web-based todo apps like Trello and Todoist didn't suit me very much. As a result, I decided to jump into some code and create a custom to-do mac app.

My basic requirements were very humble: I need a task list in which I can create, read, update and delete tasks easily. I eventually decided to go with a unix-like command line application. Unix apps are usually made in C or Shell Script. My C is pathetic at the very least and I find shell script to be.. Queer. Java was too heavyweight a language to code a simple shell utility in, so I chose to go with Python.

I had minimal experience with python in the past. I barely knew the basic language constructs and features. Luckily, python has a very shallow learning curve. About two hours with google and my python concepts were acceptable enough to start coding. Initially, python felt very much like shell script, just slightly more verbose. The lack of semicolons in python still irritates a Java programmer like me and the absence of braces makes the code feel very different compared to Java. After a few days of coding, these features started to grow on me. 

The first draft of GTD.py was a disaster. I used a text file to store all the application data and there was a ton of File I/O involved. Combine that with me using the google python fire library like an amateur and things quickly went downhill. Every time the code ran, it threw a horrendous looking python exception at my face (coming from java, python exceptions are much more beautiful compared to terrible.java.Stack.traces). Python looked like a terrible choice of language, as I could have a similar Java program up and running in about 10 minutes.

Eventually, though, my comfort with the language grew. I ditched the text based approach and decided to use an SQLite database to store the information. I also discarded python fire and chose to use argparse. These two libraries gave me a decent challenge to build the app.

The second draft came out much better than the first. The program is now usable (still needs a little refactoring). At the time of writing, I am still getting used to python programming conventions (/articles/2017/reserved\_chars as opposed to reservedChars) and the strange looking import statements. The language is still much less verbose as compared to Java and with enough practice, I may end up being more productive in Python. There's still a long way to go - I barely know the standard libraries and the functions. I also need to get to know the python runtime well enough before I start coding serious application critical components in python. The initial impression of python as a language for me was decently good. Would be interesting to see where I stand in about two to three months with the language.

Check out the GTD.py code [here](https://github.com/Aniruddha-Deb/GTD.py)

Good luck to all those starting their python journey!

\- Deb
