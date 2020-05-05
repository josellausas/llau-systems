#/usr/bin/env bash
sentry-cli releases new -p llau-systems-web $VERSION && \
sentry-cli releases set-commits --auto $VERSION
