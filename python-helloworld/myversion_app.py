from flask import Flask
from flask import json
import logging

app = Flask(__name__)

def logs():
    logging.basicConfig(filename="app.log",filemode="a",
    level=logging.DEBUG,format="%(asctime)s, %(message)s")

@app.route("/status")
def status():
    Response=app.response_class(
        response=json.dumps({ "result": "OK - healthy" }),
        status=200,
        mimetype='application/json'
        )
    endpoint_name='status'
    logs()
    logging.debug("%s has reached", endpoint_name)
    return Response

@app.route("/metrics")
def metrics():
    Response=app.response_class(
        response=json.dumps({"status":"seccess","code":0,"data": {
        "UserCount": 140,
        "UserCountActive": 23 }}),
        status=200,
        mimetype='application/json'
        )
    endpoint_name='metrics'
    logs()
    logging.debug("%s has reached", endpoint_name)
    return Response

@app.route("/")
def hello():
    endpoint_name='__main__'
    logs()
    logging.debug("%s has reached", endpoint_name)
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
