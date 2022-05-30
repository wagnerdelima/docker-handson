FROM python:3.9-slim

RUN mkdir /code
WORKDIR /code

# add all files from /heath to /code
ADD . /code

RUN apt-get update -y && apt-get install curl -y
RUN pip install -r requirements.txt

CMD ["./gunicorn.sh"]
HEALTHCHECK --interval=1s --timeout=1s --start-period=5s --retries=3 CMD curl -f http://localhost/health

EXPOSE 5000:80
