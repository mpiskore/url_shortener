FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
COPY run.sh /code/

RUN pip3 install -r requirements.txt

RUN chmod +x run.sh
COPY . /code/
