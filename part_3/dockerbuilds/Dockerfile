FROM python:3.10
LABEL maintainer="Pedro MOREIRA"
LABEL version="1.0"

RUN apt-get update
RUN apt-get install nano

RUN mkdir -p /myServer
RUN mkdir -p /log

COPY . /myServer

WORKDIR /myServer

RUN pip install --upgrade pip
RUN pip install -r /myServer/requirements.txt

VOLUME /myServer/config
VOLUME /log

EXPOSE 8080

CMD [ "python", "modelmanager.py" ]
