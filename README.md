chrisbredesen.com
=================

Source for [chrisbredesen.com](https://chrisbredesen.com) — a personal blog built with [Hugo](https://gohugo.io) using the [m10c](https://github.com/vaga/hugo-theme-m10c) theme (currently modified but will be forking and sending a PR to the developer).

Content lives in `hugo-site/content/posts/` as Markdown page bundles (each post is a directory containing `index.md` and any image assets).

## Development

```bash
cd hugo-site && hugo server   # local dev server at http://localhost:1313/
cd hugo-site && hugo          # production build to hugo-site/public/
```

## Deployment

The site is hosted on S3 + CloudFront. Scripts in `bin/` handle infrastructure and deployment:

| Script | Purpose |
|---|---|
| `bin/04-deploy.sh` | Build Hugo site, sync to S3, invalidate CloudFront cache |
| `bin/05-create-deploy-user.sh` | Create minimal IAM deploy user for CI/CD |

To deploy:

```bash
./bin/04-deploy.sh
```

The deploy script auto-detects the CloudFront distribution by domain alias. The `cb-deployer` IAM user (created by `05-create-deploy-user.sh`) has only the permissions needed to sync S3 and invalidate the CloudFront cache — suitable for use as a GitHub Actions secret.
