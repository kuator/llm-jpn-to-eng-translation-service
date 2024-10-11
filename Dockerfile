FROM python:3.12.4-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir -Ur requirements.txt

EXPOSE 8001

COPY . .
