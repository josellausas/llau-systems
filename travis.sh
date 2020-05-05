#/usr/bin/env bash
curl -sL https://sentry.io/get-cli/ | bash
sentry-cli releases new -p llau-systems-web $TRAVIS_BUILD_NUMBER && \
sentry-cli releases set-commits $TRAVIS_BUILD_NUMBER --commit "josellausas/llau-systems" && \
./test.sh && \
docker build -t zunware/llau-systems-web . && \
./push.sh
