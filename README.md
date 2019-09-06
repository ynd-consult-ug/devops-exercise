# About this repo

This is a repository used in YND Technologies recruitment process.
Based on your experience, take the following tasks and try to accomplish as many as possible.

This should not take more than few hours.
Good luck!

## Intern level

- Fork this repo
- Checkout https://github.com/MicroPyramid/Django-CRM tag 0.4.0 into it
- Prepare your own centos based Dockerfile, using uwsgi
- Prepare your own docker-compose.yml, building your own postgresql docker image

## Junior

- Add mailhog and traefik and configure everything to run behind it using localhost DNS
- Write a basic Jenkinsfile to build the app and push the images to ECR in AWS, runs coverage and publishes it to jenkins
- Reimplement wait-for-postgres.sh without using any postgres client

## Mid

- Configure deploy to local minikube in dev namespace