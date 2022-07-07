FROM python:3.10.5-alpine3.16
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /app/requirements.txt

RUN set -ex \
    && pip install --upgrade pip \  
    && pip install --no-cache-dir -r /app/requirements.txt 

WORKDIR /app