FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y apt-utils \
    build-essential git cmake autoconf libtool pkg-config \
    software-properties-common \
    python3-pip python3-dev vim wget

WORKDIR /usr/src/app
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
