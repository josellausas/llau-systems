#/usr/bin/env bash
curl -sL https://sentry.io/get-cli/ | bash
VERSION=$(sentry-cli releases propose-version)
sentry-cli releases new -p llau-systems-web $VERSION
sentry-cli releases set-commits --commit "josellausas/llau-systems@$TRAVIS_COMMIT_RANGE"
./test.sh && \
docker build -t zunware/llau-systems-web . && \
./push.sh
