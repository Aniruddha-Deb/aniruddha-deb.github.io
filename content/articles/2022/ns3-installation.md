---
title: 'Installing ns3: What worked'
publishDate: '2022-10-06T18:00:00'
categories: Programming
tags:
- Programming
- Networks
slug: ns3-installation
draft: true
---

## Prerequisites

* XCode CLT (which you should have)
* QT 5. Install via `brew install qt5`. NOTE: if you already have an updated version of Qt, you'll need to pass a different `qmake`, and brew won't link this to your system. Brew will inform you of this, and you'll manually need to pass the path to `qmake` while building. More on this later.
* Python
* ? PyBindGen - I installed this via `pip install pybindgen`, but `waf` didn't pick it up. If anyone else succeeds, let me know in the comments.

## Installation

* Download the source code, unzip with `tar -xvf` and `cd` into the directory
* Use the following command to build: `./build.py [--qmake-path=/usr/local/opt/qt@5/bin/qmake] --enable-examples --enable-tests -- --build-profile=optimized --disable-werror` (Without the stuff in the square brackets, if you don't have a newer version of Qt preinstalled, and with the stuff but excluding the square brackets if you do have a newer version).

Aaaand you're good! To test, change into the `ns-3.29` directory and do `./waf --run hello-simulator`. You should see `Hello Simulator` printed. To test NetAnim, go to the `netanim-3.108` folder and do `./NetAnim`, and you should see the NetAnim GUI pop up. 

**Update**: The python bindings are generated when you run `waf` using python2 (no idea why not with python3). To generate them, go to `ns-3.29` and run `python2 waf configure --build-profile=optimized --enable-examples --enable-tests --disable-werror` and then `./waf build`.
