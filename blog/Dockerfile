FROM ruby:2.6.3

WORKDIR /blog/app

RUN curl https://deb.nodesource.com/setup_12.x | bash && curl https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y nodejs yarn postgresql-client

ADD blog/Gemfile blog/Gemfile.lock blog/app/
RUN gem install bundler:2.2.4
RUN gem install rake:13.0.1

#RUN cd blog/app
#RUN bundle install
RUN bundle install --path blog/app

ADD blog/. blog/app

CMD blog/app/docker-entrypoint.sh
