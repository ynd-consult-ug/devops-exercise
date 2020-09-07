# About this repo

This is a repository used in YND Technologies recruitment process.
Based on your experience, take the following tasks and try to accomplish as many as possible.

This should not take more than a few hours.
Good luck!

## Intern level

1. Create your own repository using files provided in this repo.
2. Using postgresql and [docker-ruby](https://github.com/ynd-consult-ug/docker-ruby) configure the application in `./blog` to be built and start.
3. Prepare your own docker-compose.yml, with all the required services. !!Remember to use env_file with .env.!!
4. Initialize the app and make sure, that it starts

The expectation is to be able to run `docker-compose up` and have the app running using your Dockerfile and postgresql and available at http://localhost:3000

## Junior

5. Add [Traefik v2](https://containo.us/traefik/) and configure everything to run behind it using lvh.me
6. Write a basic Jenkinsfile to build and deploy the app using git clone + docker-compose up.

As an extension of intern level, the person running `docker-compose up` would also have traefik running and should be able to access wordpress via traefik.

## Mid

8. Create another Jenkinsfile to deploy everything created in the previous steps to a kubernetes cluster.
9. Use all kubernetes best practices you know.
10. Optimize layer caching of docker to speed up build times. (Can be tested via editing blog/Gemfile and adding comments inside)

As an extension of previous levels, the person checking this repo should be able to use your kubernetes manifests to deploy to an existing cluster (it's fine if it requires importing image to the node manually).

## Senior

11. Add prometheus to the docker-compose.yml. Set PROMETHEUS_EXPORTER=1 in .env, to enable metrics export. Metrics will be available at http://localhost:9394/metrics
12. Add grafana. Do not use default credentials
13. Create a dashboard rendering some of the metrics.
14. Configure autoimport of your dashboard on initial start of Grafana.

As an extension of previous levels, the person checking this repo should be able to use your docker-compose file to start the app and view a simple dashboard in grafana.

## Important

If you don't have a k8s cluster, feel free to use minikube.

Push everything you did to your repository.