# About this repo

This repo is used as part of recruitation process for YND DevOps.  
Every higher level, requires fulfilling all tasks from the previous level.  
Tasks below shouldn't take more than:

- Intern 6h
- Junior 6h
- Mid 3h

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