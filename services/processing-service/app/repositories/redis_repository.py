import redis 
import json
from config.settings import REDIS_HOST, REDIS_PORT

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

def store_meter_data(meter_id, data):
    key = f"meter:{meter_id}"
    redis_client.set(key, json.dumps(data))