FROM python:3.8-slim-buster

WORKDIR /sender

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# basic dependencies
RUN apt update 
RUN apt install -y iputils-ping

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /sender/requirements.txt
RUN pip install -r requirements.txt
COPY . /sender