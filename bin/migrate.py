#!/usr/bin/env python3
"""Migrate Hexo posts to Hugo page bundles."""

import os
import re
import shutil

HEXO_POSTS = '/Users/cbredesen/Workspaces/cbredesen/chrisbredesen.com/source/_posts'
HUGO_POSTS = '/Users/cbredesen/Workspaces/cbredesen/chrisbredesen.com/hugo-site/content/posts'

os.makedirs(HUGO_POSTS, exist_ok=True)


def fix_frontmatter(content):
    """Ensure frontmatter has opening --- delimiter."""
    if not content.startswith('---'):
        content = '---\n' + content
    return content


def convert_asset_img(content):
    """Convert Hexo asset_img shortcodes to Markdown images."""
    # {% asset_img filename.jpg "Caption text" %}
    content = re.sub(
        r'\{%\s*asset_img\s+(\S+)\s+"([^"]+)"\s*%\}',
        r'![\2](\1)',
        content
    )
    # {% asset_img filename.jpg %}  (no caption)
    content = re.sub(
        r'\{%\s*asset_img\s+(\S+)\s*%\}',
        r'![](\1)',
        content
    )
    return content


def fix_dates(content):
    """Pad dates that are missing seconds (e.g. 2016-05-22 22:12 → 2016-05-22 22:12:00)."""
    return re.sub(
        r'^(date:\s*\d{4}-\d{2}-\d{2} \d{2}:\d{2})$',
        r'\1:00',
        content,
        flags=re.MULTILINE
    )


def convert_more_tag(content):
    """Convert Hexo <!-- more --> to Hugo <!--more-->."""
    return content.replace('<!-- more -->', '<!--more-->').replace('<!-- more-->', '<!--more-->')


def migrate_post(md_file):
    slug = md_file[:-3]  # strip .md
    src_md = os.path.join(HEXO_POSTS, md_file)
    src_assets = os.path.join(HEXO_POSTS, slug)

    bundle_dir = os.path.join(HUGO_POSTS, slug)
    os.makedirs(bundle_dir, exist_ok=True)

    with open(src_md, 'r', encoding='utf-8') as f:
        content = f.read()

    content = fix_frontmatter(content)
    content = fix_dates(content)
    content = convert_asset_img(content)
    content = convert_more_tag(content)

    dest_md = os.path.join(bundle_dir, 'index.md')
    with open(dest_md, 'w', encoding='utf-8') as f:
        f.write(content)

    # Copy asset folder contents if it exists
    if os.path.isdir(src_assets):
        for asset in os.listdir(src_assets):
            src_asset = os.path.join(src_assets, asset)
            if os.path.isfile(src_asset):
                shutil.copy2(src_asset, os.path.join(bundle_dir, asset))
                print(f"  copied asset: {asset}")

    print(f"Migrated: {slug}")


def migrate_about():
    src = '/Users/cbredesen/Workspaces/cbredesen/chrisbredesen.com/source/about/index.md'
    dest_dir = '/Users/cbredesen/Workspaces/cbredesen/chrisbredesen.com/hugo-site/content/about'
    os.makedirs(dest_dir, exist_ok=True)

    with open(src, 'r', encoding='utf-8') as f:
        content = f.read()

    content = fix_frontmatter(content)

    with open(os.path.join(dest_dir, 'index.md'), 'w', encoding='utf-8') as f:
        f.write(content)
    print("Migrated: about page")


if __name__ == '__main__':
    posts = sorted(f for f in os.listdir(HEXO_POSTS) if f.endswith('.md'))
    for post in posts:
        migrate_post(post)
    migrate_about()
    print(f"\nDone. Migrated {len(posts)} posts.")
