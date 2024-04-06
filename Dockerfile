FROM docker.arvancloud.ir/python:3.11.4-slim-buster
MAINTAINER OmidAsadi
RUN apt update
ENV DEBIAN_FRONTEND="noninteractive"
RUN apt install nano
RUN mkdir -p /var/www/todo/
WORKDIR /var/www/todo/
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
RUN chmod +x entrypoint.sh
