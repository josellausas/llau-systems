#/usr/bin/env bash
curl -sL https://sentry.io/get-cli/ | bash
export VERSION=$(sentry-cli releases propose-version)
./set_version.sh && \
./test.sh && \
docker build -t zunware/llau-systems-web . && \
./push.sh
