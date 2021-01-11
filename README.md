1. Changed the paths to build files in Dockerfile to fit the Jenkins Pipeline environment.
2. Hostname now is still in Dockerfile. Along with username and password will be moved to Secrets.
3. Image can be either pushed to DockerHub or be used localy by
                adding line imagePullPolicy: Never in blog.yaml.


