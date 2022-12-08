
import redis
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
        logs = list(data['logs'])
        for word in logs:
            if word == 'ERROR' or 'Error' in word:
                flag = True
                break
        if flag:
            ## Send email notification of error occured
            requests.post('http://127.0.0.1:3000/apisendmail', json=data)

        ## Add data to the redis sorted sets
    except Exception as e:
        print(e)

    return flag

'''
while True:
    try:
        print("Waiting for incoming file")
        work = redis_connection.blpop("toWorker", timeout=0)
        boolean = analyzer(work)
    except Exception as e:
        print(f"worker loop exception: {str(e)}")

'''