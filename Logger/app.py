from flask import Flask, request, Response, jsonify
import requests
import traceback
import logging
import json


app = Flask(__name__)
#logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route("/apiv1/add", methods=['GET','POST'])
def add():
    data = request.json
    a = 0
    b = 0
    add = 0
    try:
        a = int(data['a'])
        b = int(data['b'])
        add = a + b

    except Exception as e:
        print(e)
        logs = "{0}".format(traceback.format_exc())
        dictobj = {"email": "dhrumildma@gmail.com", "logs": logs}
        data = json.dumps(dictobj)
        response = requests.post("http://127.0.0.1:6000/apiv1/update/logs", data=data)
        print(response)
    response = jsonify({'a': a, 'b': b, 'result': add})
    return response, 200


@app.route("/apiv1/divide", methods=['GET'])
def div():
    data = request.json
    a = 0
    b = 0
    div = 0

    try:
        a = int(data['a'])
        b = int(data['b'])

        if b == 0:
            raise ValueError("Divide by 0 not allowed")
        div = a / b

    except Exception as e:
        print(e)
        logs = "{0}".format(traceback.format_exc())
        dictobj = {"email": "dhrumildma@gmail.com", "logs": logs}
        data = json.dumps(dictobj)
        response = requests.post("http://127.0.0.1:6000/apiv1/update/logs", data=data)
        print(response)
    response = jsonify({'a': a, 'b': b, 'result': div})
    return response, 200


@app.route("/apiv1/file", methods=['GET', 'POST'])
def fileread():
    data = request.json
    print(data)
    try:
        filename = data['file']
        file = open(filename, 'r')
        data = file.readlines()
        data = list(data)
        print(data)
    except Exception as e:
        print(type(e))
        logs = "{0}".format(traceback.format_exc())
        dictobj = {"email": "dhrumildma@gmail.com", "logs": logs}
        data = json.dumps(dictobj)
        response = requests.post("http://127.0.0.1:6000/apiv1/update/logs", data=data)
        print(response)
    response = "hello"
    return response, 200


@app.route("/apiv1/unbound", methods=['GET'])
def unbound():
    data = request.json
    try:
        print(value)
        value = data['value']
    except Exception as e:
        print(e)
        logs = "{0}".format(traceback.format_exc())
        dictobj = {"email": "dhrumildma@gmail.com", "logs": logs}
        data = json.dumps(dictobj)
        response = requests.post("http://127.0.0.1:6000/apiv1/update/logs", data=data)
        print(response)
    return jsonify("Unbound"), 200






if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
