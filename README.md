chrisbredesen.com
=================

This repository holds source and configuration for [chrisbredesen.com](http://chrisbredesen.com).

Source is in Markdown. Sits is baked with [Hexo](https://hexo.io) using the [Tranquilpeak](https://github.com/LouisBarranqueiro/hexo-theme-tranquilpeak) theme.

Deployment
----------

Mostly this is a set of notes to remind me so I don't forget :)

  * `aws s3 sync public/ s3://chrisbredesen.com`
  * `aws cloudfront create-invalidation --distribution-id <hidden> --paths /index.html`