---
title: Vim Sutras
publishDate: '2022-10-22T09:45:00'
categories: Programming
tags:
- Programming
- Vim
slug: vim-sutras
draft: true
---

![vim setup screenshot](/articles/2022/res/vim-1.png)

-----

> When in Neovim, Do as the Luans do

Unless you're just starting out with Neovim or are extremely used to vim, it's a good idea to set up Neovim using neovim-exclusive plugins. Most of them are written in lua, and integrate more nicely with the Neovim environment (async, faster startup, support for LSP and treesitter, etc). 

My initial neovim setup was just a clone of my vim setup, but when I noticed NERDTree wasn't loading large directories quickly, I searched for a lighter, async file tree plugin for Neovim and came across NvimTree, and not long after, all my vim plugins were replaced with their neovim equivalents.

-----

> Shun character by character movements

Do not use h,j,k,l as a drop in replacement for your arrow keys: it is the vim equivalent of using a fine-tipped brush to paint your entire watercolour. Use a broad brush for the base strokes (`?`, `/`, `gg`/`G`), a finer brush for outlines (`f`, `t`) and the finest brushes for detailing (`w`, `b`, `e`, `h`, `j`, `k`, `l`)

Also, for tag-jumping, use `<C-[>` with ctags and `gf` for going to a file under the cursor. For more motions, see [this](https://www.barbarianmeetscoding.com/boost-your-coding-fu-with-vscode-and-vim/moving-blazingly-fast-with-the-core-vim-motions/)

-----

> Repeat, don't retype

Make liberal use of `;` (repeat motion) and `.` (repeat edit). They are powerful tools.

-----

> Master the nature of Vi: all else is ephemeral

Don't rely too much on plugins or keybinds: they might give a huge speedup in very specific cases, but as [The dharma of vi](https://blog.samwhited.com/2015/04/the-dharma-of-vi/) states, "With patience the man who knows how to use a snare may catch himself a hare, or a hog, or a grouse for dinner, even though the snare was not made for all these things. The man who shapes the snare to better catch only the rabbits foot will starve if no rabbit wanders by."

Also from [Vim koans](https://blog.sanctum.geek.nz/vim-koans/), "you will master vimscript when you never use it".

-----

> Vi and the shell are one

The `!` command allows you to run any shell command via Vi. 

Suppose you have a list of files in a directory `d` and you want to load in the names of only the ones starting with `en` into your file. Simply do
```
:r !ls d/en* -1
```

The [Vim koans](https://blog.sanctum.geek.nz/vim-koans/) also have a nice example of this, where they convert Markdown to HTML

-----

> Shepherd your lines with ex

ex mode is useful when line-based tasks have to be done in a non-visual manner. If I want to duplicate a method that is 5 lines above me and 3 lines long to my current position, I'd do
```
:-5,-3co.
```

Same with motions: If I want to move that method here, I'd do
```
:-5,-3mo.
```

This is also where relative line numbers shine: if you're in a file with a lot of lines, you'd need to type the entire line number (which may be 3/4 digits) twice. Instead, relative line numbers are easier to type.

-----

> Mysterious are the ways of g

Reference: [The power of `g`](https://vim.fandom.com/wiki/Power_of_g)

-----

> When in doubt, refer to the user manual

```
:h user-manual
```

And use `gf` to navigate the various subfiles in it. 

-----

Haven't posted in a while: I realized I could post about the million other things I've done recently, but I don't want to make this blog an instagram status feed.
