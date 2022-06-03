FROM python:3.9-slim

RUN mkdir /code
WORKDIR /code

RUN python -m pip install --upgrade pip && pip install psycopg2-binary
ADD . /code

CMD ["./run.sh"]
