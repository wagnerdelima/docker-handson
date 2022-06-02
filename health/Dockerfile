FROM python:3.9-slim

# create directory
RUN mkdir /code

# same as cd /code
WORKDIR /code

# add all files from /heath to /code
ADD . /code

RUN apt-get update -y && apt-get install curl -y
RUN pip install -r requirements.txt

CMD ["./gunicorn.sh"]
# monitoring
HEALTHCHECK --interval=1s --timeout=3s --start-period=5s --retries=3 CMD curl -f http://localhost/health

EXPOSE 5000:80
