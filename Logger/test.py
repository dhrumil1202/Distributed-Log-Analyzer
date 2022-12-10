
import redis
import json
import os

redis_host = os.getenv("REDIS_HOST") or "localhost"
redis_port = 6379
redis_connection = redis.StrictRedis(host=redis_host, port=redis_port, db=0)
redis_queue = "ToWorker"

work = redis_connection.blpop(redis_queue, timeout=0)


print(work[1])
work = json.loads(work[1].decode("utf-8"))
print(work)
print(type(work))