FROM ruby:2.6.3
 WORKDIR /app

 RUN curl https://deb.nodesource.com/setup_12.x | bash && curl https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && echo “deb https://dl.yarnpkg.com/debian/ stable main” | tee /etc/apt/sources.list.d/yarn.list
 RUN apt-get update && apt-get install -y nodejs yarn postgresql-client

 RUN ls
 RUN cd .. && ls
 #Gemfile Gemfile.lock /app/
 ADD Gemfile Gemfile.lock /app/

 RUN gem install bundler:2.2.4
 RUN gem install rake:13.0.1
 RUN bundle install

 ADD . /app
 CMD /app/docker-entrypoint.sh