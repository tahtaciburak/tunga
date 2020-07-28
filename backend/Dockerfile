FROM ubuntu:18.04
RUN apt-get update && apt-get install -y \
  git \
  python3-dev \
  python3-pip

ADD requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

RUN mkdir /app

COPY . /app
ENV IN_DOCKER_CONTAINER True
ENV APP_SETTINGS "project.server.config.ProductionConfig"

WORKDIR /app
RUN ["python3","manage.py","create_db"]
RUN ["python3","manage.py","init"]
RUN ["python3","manage.py","migrate"]

EXPOSE 8080
ENTRYPOINT ["python3","manage.py","runserver","-p 8080"]
