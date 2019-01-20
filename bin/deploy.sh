#!/bin/bash

PATHS='/index.html'
FOLDER='public/'
BUCKET='chrisbredesen.com'

# look for --invalidate-all (just kidding this is ugly af)
if [ "$1" ]; then
    PATHS='/*'
fi

echo Syncing $FOLDER to bucket $BUCKET
aws s3 sync $FOLDER s3://$BUCKET

echo Creating CloudFront invalidation on paths $PATHS
aws cloudfront create-invalidation --distribution-id E3MIM4G6ZCVGI8 --paths $PATHS