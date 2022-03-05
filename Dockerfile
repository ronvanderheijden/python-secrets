ARG ALPINE_VERSION='3.15'
FROM python:alpine$VERSION AS base

RUN apk add --no-cache --upgrade --no-progress bash gnupg \
    && python -m pip install --no-cache-dir --upgrade pip python-gnupg

WORKDIR /home

COPY cmds /usr/local/sbin
