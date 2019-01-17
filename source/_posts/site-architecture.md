---
title: Site Architecture
date: 2016-05-22 22:34
categories:
  - Personal
tags:
  - meta
  - hexo
---

The way it works is I have a bunch of Markdown that gets processed by [Hexo](https://hexo.io/) and synced to an S3 bucket. This is a process that was ostensibly made mainstream by Jekyll but is now supported by a lot of different tools in the same genre.

<!-- more -->

I started awhile back with [Awestruct](http://awestruct.org/) but could never get the Ruby dependencies worked out.

Then I took a look at [Jekyll](https://jekyllrb.com/) since it is by most measures the most popular static site generator. What I dislike about Jekyll is that the tool and the theme are coupled in a way that seems like it'll make upgrading one or the other in the future difficult.

[Pelican](http://getpelican.com/) looked pretty good and I got something reasonable out of it but there are just too few themes from which to choose. None called to me. I did find a nice one but found it cumbersome to customize.

Frustrated, I returned to this directory of tools and noticed Hexo which I don't recall having seen before. It's Node-based because everything these days is but I gave it a shot anyway. The themes are nicely separated from the tool and the site content and it was reasonably easy to get going. So, here we are.

The theme I'm using is [tranquilpeak](https://github.com/LouisBarranqueiro/hexo-theme-tranquilpeak) and the background [photo](/assets/images/davie_rain.jpg) is my original work.

I have not yet worked out the mismatch between the line breaks in the source Markdown and how they render in HTML...
