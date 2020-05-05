#/usr/bin/env bash
curl -sL https://sentry.io/get-cli/ | bash
export VERSION="llausys-web@$TRAVIS_BUILD_NUMBER"
sentry-cli releases new -p llau-systems-web $VERSION && \
sentry-cli releases set-commits $VERSION --commit "josellausas/llau-systems" && \
./test.sh && \
docker build -t zunware/llau-systems-web . && \
./push.sh
