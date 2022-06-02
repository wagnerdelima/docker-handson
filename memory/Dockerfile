FROM python:3.9-slim

RUN mkdir /code
WORKDIR /code

RUN python -m pip install --upgrade pip && python -m pip install psutil

ADD . /code

CMD ["./run.sh"]
