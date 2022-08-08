FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /docker_app
ADD . /docker_app
RUN pip3 install -r requirements.txt

