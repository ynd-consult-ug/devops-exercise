FROM yndconsult/docker-ruby:2.6.3-centos7

WORKDIR "/app"

RUN yum install postgresql-devel -y 
RUN curl -sL https://rpm.nodesource.com/setup_10.x | bash - && yum install nodejs -y
RUN curl -sL https://dl.yarnpkg.com/rpm/yarn.repo | tee /etc/yum.repos.d/yarn.repo && yum install yarn -y
RUN gem install bundler

COPY yarn.lock Gemfile* ./

RUN yarn upgrade @rails/webpacker
RUN bundle install

COPY . .
ENV DATABASE_NAME="blog_backend"
ENV DATABASE_PASSWORD="blog_backend"
ENV DATABASE_USERNAME="blog_backend"
CMD /app/docker-entrypoint.sh
