import redis
import json
from config.settings import REDIS_HOST, REDIS_PORT

redis_client = redis.Redis(
    host=REDIS_HOST, 
    port=REDIS_PORT,
    decode_responses=True
)

def get_meter_data(meter_id):
    key = f"meter:{meter_id}"

    data = redis_client.get(key)

    if not data:
        return None
    
    return json.loads(data)


def get_all_meters():
    keys = redis_client.keys("meter:*")

    meters = []

    for key in keys:
        data = redis_client.get(key)
        meters.append(json.loads(data))
    
    return meters
