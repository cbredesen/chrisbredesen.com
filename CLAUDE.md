# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Goal

This is a personal brand static site currently built with Hexo.js. The goal is to migrate it to Hugo (similar to the setup used in `../estatesofpinewood.org`) while preserving the hueman theme design, all posts, and associated assets.

## Current Stack (Hexo)

### Commands

```bash
hexo generate        # Build static site into public/
hexo server          # Local dev server at http://localhost:4000
hexo new post "Title" # Create new post (uses scaffolds/post.md)
hexo clean           # Remove generated public/ and db.json
```

### Deploy

```bash
bin/deploy.sh                    # Sync public/ to S3 + CloudFront invalidation
bin/deploy.sh --invalidate-all   # Full CloudFront cache invalidation
```

Deployment targets S3 bucket `chrisbredesen.com` with CloudFront distribution `E3MIM4G6ZCVGI8`.

## Content Structure

- `source/_posts/` — 18 markdown posts with associated asset folders (post asset folders enabled)
- `source/about/` — About page
- `source/assets/` — Static assets
- `themes/hueman/` — Active theme (ppoffice/hexo-theme-hueman, based on WordPress Hueman by AlxMedia)

### Post Format

```markdown
title: Post Title
date: YYYY-MM-DD HH:MM:SS
tags:
---
```

Posts use permalink structure `/:year/:month/:title/`. Each post may have a same-named directory alongside it for image assets.

## Theme (Hueman)

The hueman theme uses EJS templates (`themes/hueman/layout/`), Stylus for CSS (`themes/hueman/source/css/`), and includes Insight search, Font Awesome, and jQuery. Theme config lives in `themes/hueman/_config.yml`.

## Hugo Migration Notes

When migrating to Hugo:
- Preserve hueman theme visuals and layout structure
- Maintain existing permalink format (`:year/:month/:title/`) to avoid breaking links
- Keep post asset folder structure — images live alongside posts
- Match the S3 + CloudFront deployment pattern used in `../estatesofpinewood.org`
- Atom feed at `/atom.xml` (20 posts) should be preserved
