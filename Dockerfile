FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code/
# COPY requirements.txt requirements.txt
# COPY manage.py manage.py
# COPY url_mapper url_mapper
# COPY url_shortener url_shortener

RUN pip install -r requirements.txt
