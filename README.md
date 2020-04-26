# Llau Systems

[![Build Status](https://travis-ci.com/zunware/llau-systems.svg?token=pPjgy1gbyCJtL7uhrXTa&branch=develop)](https://travis-ci.com/zunware/llau-systems)

## Install and run

1. Create a virtualenv at `env/` and activate
2. Install deps with `pip install -r requirements.txt`
3. Run server with `manage.py runserver`

## Run Tests

`./manage.py test`

## Run Cypress Tests
1. Install cypress with `yarn install`
2. Run Cypress : `yarn run cypress open`

# Resources
- https://github.com/BulmaTemplates/bulma-templates/blob/master/templates/hero.html
- https://bulmastyle.com
- https://bulma.style/film/dist/
- https://cssninjastudio.github.io.
- https://bulmatemplates.github.io/bulma-templates/templates/showcase.html
- https://bulmatemplates.github.io/bulma-templates/templates/personal.html
- https://bulmathemes.com
- https://github.com/cssninjaStudio/fresh

# Kubernetes

Run in Kubernetes
`kubectl run llausys-web --env="DB_PASSWORD=''" --env="DB_HOST=localhost" --image=zunware/llau-systems-web:latest --port 8000`

`k apply -f postgres-deployment.yml && k apply -f django-deployment.yml`