FROM yndconsult/docker-ruby:2.6.3-centos7
WORKDIR "/blog/app"

RUN curl –sL https://rpm.nodesource.com/setup_10.x | bash -
RUN curl -sL https://dl.yarnpkg.com/rpm/yarn.repo | tee /etc/yum.repos.d/yarn.repo

RUN yum install yarn nodejs postgresql-devel bundler -y
COPY ./blog/yarn.lock /blog/Gemfile ./

RUN yarn upgrade @rails/webpacker
RUN bundle install

COPY /blog/. /blog/app

ENTRYPOINT /blog/app/docker-entrypoint.sh