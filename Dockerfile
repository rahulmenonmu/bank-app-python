FROM python:alpine3.7
COPY . /app
WORKDIR /app
CMD python main.py