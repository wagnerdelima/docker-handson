from threading import Lock

from flask import Flask


app = Flask(__name__)

lock = Lock()
counter = 0


@app.route("/health", methods=['GET'])
def hello_world():
    global counter

    with lock:
        counter += 1
    if counter > 5:
        raise Exception

    return "<p>Healthy: OK!</p>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
