FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1 
WORKDIR /docker_app 
COPY requirements.txt /docker_app/ 
RUN pip install -r requirements.txt 
COPY . /docker_app/ 