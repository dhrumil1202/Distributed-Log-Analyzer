from flask import Flask, request, Response, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(filename='record.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


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
        logging.exception(e)
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
        logging.exception(e)
    response = jsonify({'a': a, 'b': b, 'result': div})
    return response, 200


@app.route("/apiv1/file", methods=['GET'])
def fileread():
    data = request.json

    try:
        filename = data['file']
        file = open(filename, 'r')
        data = file.readlines()
        data = list(data)

    except Exception as e:
        print(e)
        logging.exception(e)
    response = jsonify(data)
    return response, 200


@app.route("/apiv1/unbound", methods=['GET'])
def unbound():
    data = request.json
    try:
        print(value)
        value = data['value']
    except Exception as e:
        print(e)
        logging.exception(e)
    return jsonify("Unbound"), 200






if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
