FROM python:3.8

RUN mkdir /code
WORKDIR /code

COPY src/requirements.txt /code/
COPY src/run.sh /code/

RUN pip3 install -r requirements.txt

COPY src /code/
