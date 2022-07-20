FROM python:3.9-alpine
LABEL maintainer="stasyanzayac@gmail.com"

WORKDIR /app/
ADD . /app
RUN apk update

ENV PYTHONUNBUFFERED 0

RUN apk add bash vim
RUN apk add g++ gcc
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

ENV PYTHONPATH "$PYTHONPATH:/app/src"
RUN echo $PYTHONPATH
ENTRYPOINT ["python", "-u", "src/main.py"]
