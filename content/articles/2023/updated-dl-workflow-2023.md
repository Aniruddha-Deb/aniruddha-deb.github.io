Title: My (updated) DL workflow for 2023
Date: 2023-06-04 01:00
Category: Programming
Tags: Programming, Machine Learning, Deep Learning
Slug: updated-dl-workflow-2023

Remember last semester, where I said this?

<center>
<img width="600px" src="/articles/2022/res/cs_degree.png">
</center>

That went pretty well. Much better than I expected it to go :) I also used the 
HPC DL environment a lot, across 4 courses that I did (COL380, COL772, COL775 
and COD310). It was so used that at a point I had four different GPU's allocated
just for running tasks for these different courses.

A lot could be done better, though. Since I have my summer ahead of me, I
decided to clean house for the next semester

## The secret life of software

After an OS course that delved deep into the linux kernel, I'm qualified to 
talk about this. For software-specific stuff, the relevant linux directories
are structured as follows:

```bash
/ # Root - primary hierarchy
`- bin # where your executables go
`- include # where header files go
`- lib # where libraries go
`- home # home directories of users
|  `- aniruddha # home directories of users
|     `- .local # User-specific tertiary hierarchy
|     |  `- bin
|     |  `- include
|     |  `- lib
|     `- .conda
|     |  `- envs
|     |     `- dl # a single environment folder
|     |        `- bin
|     |        `- include
|     |        `- lib
|     `- .config # directory containing config files
|     `- .bashrc # sourced on every login shell
|     `- scratch -> /scratch/aniruddha # HPC specific scratch directory
|
`- usr # Unix System Resources - Secondary Hierarchy, read only stuff for users
|  `- bin
|  `- include
|  `- lib
|  `- local # Tertiary hierarchy - has it's own bin, include, lib, etc
|  `- share # Architecture Independent (shared) data
`- opt # Optional software
```

The `PATH` variable's contents now make a lot more sense. An `echo $PATH` on a
unix box will usually have all the `bin` directories shown above, and doing a
`echo $LD_LIBRARY_PATH` will have all the `lib` directories above. It's simple,
intuitive and has been working for half a century now. More details can be found
[here](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html).

Let's say that we don't have super-user privileges. This brings two challenges:
- **The only directory above that we can write to is our home directory**.
  That's it. Any software/libraries/headers that we need to install need to be
  installed in `.local` and added to path/symlinked through
- If a binary already exists in `/bin` or `/usr/bin`, that would be registered
  by the system, especially if it needed an older version. This is visible
  in HPC, which has super-old versions of `git` (1.8x) and `conda` (5.x).

Even when it comes to modules, HPC doesn't have the latest `gcc` (stuck at 9)
or modern build tools, such as `cmake` or `ninja`. There is no clean way to 
even install these. The [HPC website](https://supercomputing.iitd.ac.in/?soft) 
mentions two options that you can take in this event:

1. Install the software in your own account (`$HOME`)
2. Request installation, via your supervisor.

2 would be a good option if it didn't have a turnaround time of over a month,
so the only sane thing to do is 1.

## Install software locally

This is easier than it sounds. HPC runs CentOS 7, which uses `yum` as it's 
package manager, so installing software should be as easy as doing `yum install 
<packagename> --local`, right?

Nope.

yum doesn't support doing this natively. [After some research](https://stackoverflow.com/questions/36651091/how-to-install-packages-in-linux-centos-without-root-user-with-automatic-depen), 
you can get yum to install things locally, but it's not worth the effort. `dnf`
isn't installed, neither is any other package manager, so this turns up a dead
end.

> #### Aside: Package Managers
> 
> What I had been doing so far was to build software from source if needed, and
> then pass the installation directory using a flag in the `make install` step.
> This is _(a)_ super hard and _(b)_ unsustainable. (a) because you'd need to 
> take into account all of the package's dependencies, and (b) because you'd 
> need to update the package if a newer version came around. 
> 
> Package managers take away all of this pain by handling the dependency 
> management and updates on their own. So what we're really looking for is **a 
> package manager that manages it's repository of packages in .local and, ipso 
> facto, can be run without superuser privileges.**

## (Mini)Conda to the rescue

The second answer in the StackExchange thread linked above recommended using
`conda` as a package manager, and that's what was finally done. However, the 
`conda` version as mentioned above is outdated, and since we want to use the
most up to date versions of packages, that would defeat the purpose.

To fix this, I installed miniconda locally in `$HOME/.local/opt/miniconda3`, 
following the good directory structure above. `miniconda3` is an open-source 
conda variant and picks up right where `conda` left off: it has access to all 
my old environments, and also uses the preferences in my `.condarc` to make
new environments in `scratch/conda_data/envs`, so that others can also use 
them.

What about keeping miniconda up to date? _Miniconda updates itself, so we don't 
need to do anything!_ conda also launches the `base` environment by default, so 
all we need to do is prepend the base conda environment's `bin` to our `PATH`,
and we can use `conda` to manage our executables!

## What now?

Let's update git, gcc, g++ and get cmake and node
```bash
conda install -c conda-forge git gcc gxx cmake nodejs==18.5.0
```

Let's also install neovim. Unfortunately there isn't a conda package for this
(there was one, but that was for neovim python bindings), so I had to manually
download the appimage from [here](https://github.com/neovim/neovim/releases/download/stable/nvim-linux64.tar.gz) 
and move the files to the right locations. Once that was done, I installed packer
to the right place, and copied my config over. Everything worked as expected 
after that.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr"><a href="https://twitter.com/Neovim?ref_src=twsrc%5Etfw">@neovim</a> is goated. <a href="https://twitter.com/code?ref_src=twsrc%5Etfw">@code</a> is bloated.</p>&mdash; Aniruddha Deb (@hairband_dude) <a href="https://twitter.com/hairband_dude/status/1665143467079507968?ref_src=twsrc%5Etfw">June 3, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

After that, I made an environment for PyTorch 2. It's a bit too late now to
test out `torch.compile`, but I will tomorrow on a couple of models. I also 
wanted to develop [pajamas](https://github.com/Aniruddha-Deb/pajamas) further,
which I'll probably do sooner or later.

And with that, I'm ready to become a researcher for the next two semesters :)

## Other things

[Amsterdam is Beautiful](https://aniruddhadeb.com/articles/2022/intern-inferno.html#intern-inferno)

![random bridge sunset](res/amsterdam.jpg)

So is Rotterdam

![erasmus bridge](res/rotterdam.jpg)

So is Antwerp

![grote markt](res/antwerp.jpg)
