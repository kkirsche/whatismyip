FROM python:3.5.2
MAINTAINER kev.kirsche@gmail.com

COPY . /app

EXPOSE 5000
ENTRYPOINT ["python3", "/app/ip.py"]
