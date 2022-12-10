
import redis
import time as t
import json
import os
import requests

redis_host = os.getenv("REDIS_HOST") or "localhost"
redis_port = 6379
redis_connection = redis.StrictRedis(host=redis_host, port=redis_port, db=0)
redis_queue = "ToWorker"

def analyzer(data):

    flag = False
    print(data)

    try:
        email = data['email']
        logs = data['logs'].split(" ")
        for word in logs:
            print(word)
            if word.upper == 'ERROR' or 'ERROR' in word.upper:
                flag = True
                break
        print(flag)
        if flag:
            ## Send email notification of error occured
            data = json.dumps(data)
            response = requests.post('http://127.0.0.1:3000/apisendmail', data=data)
            print(response)

        ## Add data to the redis sorted sets
    except Exception as e:
        print(e)

    return flag


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
                data = json.dumps(data)
                response = requests.post('http://127.0.0.1:3000/apisendmail', data=data)
                print(response)

    except Exception as e:
        print(f"worker loop exception: {str(e)}")
    t.sleep(2)
