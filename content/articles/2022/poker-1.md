Title: On Poker style games
Date: 2022-08-07 15:30
Category: Mathematics
Tags: Mathematics, Probability, Games
Slug: poker-1
Status: draft

<link rel="stylesheet" type="text/css" href="res/spoiler.css">

For the upcoming intern season interviews,

## Some elementary information theory

<blockquote class='spoiler'>
<div class='spoiler-prompt'> <b>SPOILER</b>: mouseover/tap to view</div>
<div class='spoiler-text'> checking if math works here: $$\int_0^5 x^2 dx$$</div></blockquote>

## Footnotes

Pelican is an amazing CMS: powerful enough to do anything, while being simple and flexible enough to be extensible when needed. The spoiler tags were generated using the following CSS:

```css
.spoiler-prompt {
    color: gray;
}

.spoiler-text {
    display: none;
}

.spoiler:hover .spoiler-text {
    display:block;
}

.spoiler:active .spoiler-text {
    display:block;
}

.spoiler:hover .spoiler-prompt {
    display:none;
}

.spoiler:active .spoiler-prompt {
    display:none;
}

.spoiler:hover {
    overflow-y: auto;
}
```

To create a spoiler, simply include the following `<link>` after the title block:
```
<link rel="stylesheet" type="text/css" href="res/spoiler.css">
```

and use a blockquote element with class `spoiler`, with a spoiler prompt and text to create one
```
<blockquote class='spoiler'>
<div class='spoiler-prompt'> <b>SPOILER</b>: mouseover/tap to view</div>
<div class='spoiler-text'>Spoiler text goes here</div></blockquote>
```

Most importantly, there are no issues with math in the spoiler-text tag :)