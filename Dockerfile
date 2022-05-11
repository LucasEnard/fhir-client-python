# syntax=docker/dockerfile:1

FROM python:3.8.3

WORKDIR /code

COPY . /code

RUN python3 -m pip install -r requirements.txt
