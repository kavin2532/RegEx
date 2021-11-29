FROM elixir:latest

RUN apt-get update && \
    apt-get install -y postgresql-client && \
    apt install curl -y && \
    apt install nodejs -y && \
    apt install npm -y && \
    mix local.hex -y && \
    apt-get update && \
    mix local.hex --force && \
    mix archive.install hex phx_new 1.5.3 --force && \
    mix local.rebar --force


ENV APP_HOME /app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

CMD ["mix", "phx.server"]
