from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route("/status")
def status():
    Response=app.response_class(
        response=json.dumps({ "result": "OK - healthy" }),
        status=200,
        mimetype='application/json'
        )
    endpoint_name='status'
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
    logging.debug("%s has reached", endpoint_name)
    return Response

@app.route("/")
def hello():
    endpoint_name='__main__'
    logging.debug("%s has reached", endpoint_name)
    return "Hello World!"

if __name__ == "__main__":
    #Stream logs to app.log file in the main application inside the if clause
    logging.basicConfig(filename="app.log",filemode="a",
        level=logging.DEBUG,format="%(asctime)s, %(message)s")
    #filemode=a is the default and it's working just fine for all cases
    app.run(host='0.0.0.0')
