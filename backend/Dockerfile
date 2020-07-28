FROM ubuntu:18.04
RUN apt-get update && apt-get install -y \
     python3-dev \
     build-essential libssl-dev libffi-dev \
     libxml2-dev libxslt1-dev zlib1g-dev swig \
     python3-pip git
RUN CFLAGS="-Wno-narrowing" pip3 install cld2-cffi

ADD requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

RUN pip3 install sklearn
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
