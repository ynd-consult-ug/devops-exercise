# About this repo

This is a repository used in YND Technologies recruitment process.
Based on your experience, take the following tasks and try to accomplish as many as possible.

This should not take more than a few hours.
Good luck!

## Intern level

1. Fork this repo
2. Checkout https://github.com/MicroPyramid/Django-CRM tag 0.4.0 into it
3. Prepare your own centos based Dockerfile, using uwsgi
4. Prepare your own docker-compose.yml, building your own postgresql docker image

The expectation is to be able to run `docker-compose up` and have Django-CRM running using your Dockerfile (with uwsgi) and the postgresql you setup.

## Junior

5. Add mailhog and traefik and configure everything to run behind it using /etc/hosts DNS entries
6. Write a basic Jenkinsfile to build the app
7. Reimplement wait-for-postgres.sh without using any postgres client (f.e. with netcat)

As an extension of intern level, the person running `docker-compose up` would also have traefik and mailhog running.

## Mid

8. Extend the jenkinsfile to include everything created in the previous steps to a local minikube in dev namespace
