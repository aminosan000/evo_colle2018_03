FROM python:3.6-slim
MAINTAINER "Type your name."
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install gcc default-libmysqlclient-dev
RUN pip install Flask mysqlclient sqlalchemy
RUN mkdir /var/www
COPY templates /var/www/templates
COPY python /var/www
WORKDIR /var/www
CMD python app.py
