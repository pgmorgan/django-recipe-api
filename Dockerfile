FROM        python:3.8-buster
LABEL       maintainer="Peter Morgan"
ENV         PYTHONUNBUFFERED 1
RUN         apt-get update
RUN         apt-get install -y --no-install-recommends postgresql-client
RUN         rm -rf /var/lib/apt/lists/*
WORKDIR     /usr/src/app
COPY        ./requirements.txt  ./requirements.txt
RUN         pip install -r ./requirements.txt
COPY        ./app   ./
RUN         adduser --disabled-password --gecos '' user
USER        user