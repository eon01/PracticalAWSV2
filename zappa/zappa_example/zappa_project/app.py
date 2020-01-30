from flask import Flask, Response, json, request
import requests
import boto3
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World !'

@app.route('/ping', methods=["POST"])
def ping():
    resp_dict = {}

    if request.method == "POST":
        data = request.form
        domain = data.get("domain", "")

        try:
            result = requests.get(domain).elapsed.total_seconds()
            resp_dict = {"result": result, "response": "200"}
            response = Response(json.dumps(resp_dict), 200)

        except Exception as e:
            resp_dict = {"result": "error", "response": "408"}
            response = Response(json.dumps(resp_dict), 408)        

            client = boto3.client('sns')
            client.publish(
                TopicArn="arn:aws:sns:eu-west-1:xxxxxxxxxxxxxxxxx:zappa_example",
                Message="website %s is down" % str(domain),
            )




    return response
if __name__ == "__main__":
    app.run()
























































