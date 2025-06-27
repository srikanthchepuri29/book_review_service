import redis
import json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def get_cached_books():
    try:
        data = r.get("books")
        if data:
            return json.loads(data)
    except redis.exceptions.ConnectionError:
        print("Redis is down.")
    return None

def set_cached_books(data):
    try:
        r.set("books", json.dumps(data), ex=60)
    except redis.exceptions.ConnectionError:
        print("Redis is down.")
