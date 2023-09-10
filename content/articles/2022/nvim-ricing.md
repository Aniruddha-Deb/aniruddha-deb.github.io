---
title: Neovim Ricing
publishDate: '2022-09-25T17:00:00'
categories: Programming
tags:
- Programming
- Systems
slug: nvim-ricing
---

While pruning a bug in my server, I had to debug my code on Manjaro, which was getting tedious. I'd installed Neovim, so the rational step would be to install Sublime and forget about neovim.

Right?

Nope. Let's install Neovim on Mac instead and try moving to it!

![neovim](/articles/2022/res/neovim.png)

## Sprucing up Neovim

Neovim is actually a nice editor, once you install a bunch of plugins via arcane terminal magic (what else gives people feelings of power, amirite?). The only difference I see between Neovim and good ol' vim is that Neovim supports all the old vim plugins, but also supports Lua plugins as well (and is asynchronous, but I don't notice that in practice).

It also has Language Server Protocol support and tree-sitter and a bunch of other useful stuff which I'll get around to eventually using, but are just magic for now.

## Plugins used

* `preservim/nerdtree`
* `vim-airline/vim-airline`
* `tanvirtin/monokai.nvim`
* `airblade/vim-gitgutter`
* `ryanoasis/vim-devicons`
* `Xuyuanp/nerdtree-git-plugin`

And `vim-plug` for installing all of them. Note that `vim-devicons` needs the nerdicons patched font. I use Meslo LG S, because it's basically Open-Source Menlo, and I'm too used to Menlo by this point to quit. Interestingly, my kitty config doesn't use this parameter anywhere, but still manages to pick up the glyphs from the right font... Omoshiroi.

## Roadmap

I still need to work on LSP integration (installed `ccls` today), but will do that at a later time. There are still a lot of things to move over (If I do choose to move over), some of them are:

* LSP's for C,C++,Python,Rust
* Learn the buffer vs tabs philosophy (I used tabs extensively previously in vim)
* Multi cursor vs macros... Get used to macros
* Port my Competitive Programming setup over
* VimLaTeX installation

And that's it, I guess. Terminals are probably why I'd switch over (Sublime terminals just seem half-baked, and it's much nicer using nvim+kitty than ctrl-tabbing with sublime), and nicer keyboard integration in nvim. Most of my original reasons for [switching to sublime](https://aniruddhadeb.com/articles/2021/sublime-text-setup) are now mitigated, and I do have the skill to improve my vim-jutsu.

## Footnotes

Short and sweet blog post, because it's Minors week!

Also, I might start posting these on Hacker News and Reddit

Aaaand debating whether to create a twitter as well for that added publicity. Devs with it seem to do a lot better than those without it. Even John Carmack has a twitter :^
