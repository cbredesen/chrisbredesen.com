aws s3 sync public/ s3://chrisbredesen.com
aws cloudfront create-invalidation --distribution-id E3MIM4G6ZCVGI8 --paths "/*"