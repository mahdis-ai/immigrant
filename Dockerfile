FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /immigrant
WORKDIR /immigrant
ADD requirements.txt /immigrant/
RUN pip install --upgrade pipenv && pip install -r requirements.txt
ADD . /immigrant/