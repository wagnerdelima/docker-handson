from threading import Lock
from collections import namedtuple
from os import getenv

from flask import Flask


app = Flask(__name__)

lock = Lock()
counter = 0


ApplicationStatus = namedtuple('ApplicationStatus', ['healthy'])
app_status = ApplicationStatus(healthy=bool(getenv('HEALTHY', False)),)


@app.route("/health", methods=['GET'])
def hello_world():
    global counter

    with lock:
        counter += 1
    if not app_status.healthy and counter > 5:
        raise Exception

    return "<p>Healthy: OK!</p>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
