FROM python:3.10
LABEL maintainer="Pedro MOREIRA"
LABEL version="1.0"

RUN apt-get update
RUN apt-get install -y \
    nano \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /myServer

COPY . /myServer

WORKDIR /myServer

RUN pip install --upgrade pip
RUN pip install -r /myServer/requirements.txt

VOLUME /myServer/config

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "frontend/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]