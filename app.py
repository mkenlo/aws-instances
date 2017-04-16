from flask import Flask, render_template, jsonify, request
import boto3
import json


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/getInstances", methods=['POST'])
def getInstances():
    try:

        data = json.loads(request.data.decode())
        client = boto3.client(
            'ec2',
            aws_access_key_id=data['key'],
            aws_secret_access_key=data['secretkey'],
            region_name='us-east-1')
        response = client.describe_instances(
            MaxResults=10, DryRun=False)
        print response
        return jsonify(result=response)

    except Exception, e:
        return jsonify(status='ERROR', message=str(e))


if __name__ == '__main__':
    app.secret_key = 'secret_12345678_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
