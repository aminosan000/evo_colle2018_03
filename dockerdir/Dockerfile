FROM python:3.6-slim
MAINTAINER "Type your name."
RUN mkdir /var/www
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install gcc
RUN apt-get -y install default-libmysqlclient-dev
RUN pip install Flask
RUN pip install mysqlclient
RUN pip install sqlalchemy
RUN pip install sqlalchemy-utils
COPY templates /var/www/templates
COPY python /var/www
WORKDIR /var/www
CMD python app.py
