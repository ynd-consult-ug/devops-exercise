FROM yndconsult/docker-ruby:2.6.3-centos7

WORKDIR "/app"

COPY . .

RUN curl -sL https://rpm.nodesource.com/setup_10.x | bash -
RUN yum install nodejs -y
RUN curl -sL https://dl.yarnpkg.com/rpm/yarn.repo | tee /etc/yum.repos.d/yarn.repo
RUN yum install yarn -y
RUN yum install postgresql-devel -y
EXPOSE 3000
CMD /app/docker-entrypoint.sh