#/usr/bin/env bash
coverage run --source=apps ./manage.py test && \
coveralls
