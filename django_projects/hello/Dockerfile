FROM python:3.8

ENV PYTHONDONTWRITBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.lock /code/
RUN pip install requirements.txt

COPY . /code/