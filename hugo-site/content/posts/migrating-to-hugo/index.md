---
title: Migrating to Hugo
date: 2026-04-14 00:00:00
categories:
  - Personal
tags:
  - meta
  - hugo
  - hexo
  - ai
---

*The entirety of (the remainder of) this post was written by Claude Sonnet. --CB*  

If you look back at my [Site Architecture](/2016/05/site-architecture/) post from a decade ago, you'll see I already went through the static site generator evaluation process once. That led me to Hexo, which served me well for a long time. But Hexo has aged, and so I've migrated to [Hugo](https://gohugo.io/).

<!--more-->

The immediate trigger was a combination of Node dependency rot and a general sense that the Hexo ecosystem had quietly stagnated. Plugins with abandoned repos, a theme I'd grown attached to that hadn't been touched in years, and a build process that felt increasingly creaky. Hugo, by contrast, is a single Go binary with no dependency chain to manage. That's appealing.

The migration itself was almost entirely done by [Claude Code](https://claude.ai/code) — Anthropic's agentic coding tool. I gave it the goal, pointed it at my existing Hexo source, and told it to look at another Hugo site I maintain ([estatesofpinewood.org](https://estatesofpinewood.org)) for reference. It handled converting the front matter, restructuring the content directory layout, threading through the permalink format so existing URLs wouldn't break, and building out a custom theme that preserved the general look and feel I wanted.

The theme situation is different this time. Instead of adopting something off the shelf and fighting to customize it, I described what I wanted — a clean sidebar layout, a specific color palette — and the theme was built to spec. That's a workflow I couldn't have done practically before LLMs. Writing CSS and template code from scratch for a one-person blog would have been a yak shave too far in prior years.

There are still some rough edges I'll clean up over time. But the core migration is done: 18 posts, all assets, the same S3 + CloudFront deployment pipeline, and a build process I can actually reason about.

It's a little funny to have a post about switching static site generators right next to a post about agentic engineering. The tooling that made this migration tractable in a weekend is a pretty good illustration of what that article was pointing at.
