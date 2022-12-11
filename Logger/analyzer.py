from trycourier import Courier
import redis
import time as t
import json
import os
import requests

redis_host = os.getenv("REDIS_HOST") or "localhost"
redis_port = 6379
redis_connection = redis.StrictRedis(host=redis_host, port=redis_port, db=0)
redis_queue = "ToWorker"
client = Courier(auth_token="pk_prod_JGDEDHYZYD4SJCJ9AE5N6GC0CDRJ")



while True:
    try:
        print("Waiting for incoming file")
        work = redis_connection.blpop(redis_queue, timeout=0)
        if len(work) > 1:
            data = json.loads(work[1].decode("utf-8"))

            print(data)

            email = data['email']
            logs = data['logs'].split(" ")
            print(logs)
            for word in logs:
                print(word)
                if word == 'Error' or 'Error' in word:
                    flag = True
                    break
            print(flag)
            if flag:
                ## Send email notification of error occured
                #data = json.dumps(data)
                log = data['logs']
                test = "something {0}".format(log)
                print(test)
                resp = client.send_message(
                    message={
                        "to": {
                            "email": email
                        },
                        "content": {
                            "title": "Error Notification",
                            "body": "Error Occured {0}".format(log)
                        },
                        "data": {
                            "log": str(data['logs'])
                        }
                    }
                )
                print(resp)

    except Exception as e:
        print(f"worker loop exception: {str(e)}")
    t.sleep(2)
