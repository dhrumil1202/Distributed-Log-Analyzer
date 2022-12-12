import json
import time
import os
from datetime import datetime
from flask import Flask, request, Response, jsonify
import firebase_admin
from firebase_admin import credentials, db
import redis

cred = credentials.Certificate("distributed-log-firebase-adminsdk-1881r-6a1ff5813a.json")
firebase_admin.initialize_app(cred,  {
    'databaseURL': "https://distributed-log-default-rtdb.firebaseio.com/"
})

redis_host = os.getenv("REDIS_HOST") or "localhost"
redis_port = 6379
redis_connection = redis.StrictRedis(host=redis_host, port=redis_port, db=0)
redis_queue = "ToWorker"



app = Flask(__name__)
#firebase = firebase.FirebaseApplication("https://distributed-log-default-rtdb.firebaseio.com/", None)

#logs_ref = db.collection('Logs')

@app.route("/apiv1/update/logs", methods=['GET','POST'])
def updatelogs():
    data = json.loads((request.data).decode("utf-8"))

    email = data['email']
    logs = data['logs']

    username = email.split("@")[0]
    currenttime = str(time.strftime("%H-%M-%S", time.localtime()))
    today = str(datetime.today().strftime('%Y-%m-%d'))

    reference = "/{0}/{1}/{2}".format(username, today, currenttime)

    ref = db.reference(reference)
    ref.set(data)
    redis_data = json.dumps(data)
    redis_connection.lpush(redis_queue, redis_data)

    return "done", 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)