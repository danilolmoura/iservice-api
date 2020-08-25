FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=nonintercative

RUN apt update -y && \
    apt install -y python-pip python-dev

FROM python:3.8-alpine

COPY ./requirements.txt iservice-api/requirements.txt

# Solution to avoid psycopg2 problem
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 apk add geos-dev && \
 python -m pip install -r /iservice-api/requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . iservice-api/

WORKDIR iservice-api/

# Expose port
EXPOSE 5000

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]