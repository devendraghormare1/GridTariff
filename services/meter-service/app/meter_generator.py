import random 
import time

def generate_meter_event():
    meter_id = f"MTR{random.randint(1,5):03d}"

    event = {
        "meter_id": meter_id,
        "usage_kwh":round(random.uniform(0.5, 3.0), 2),
        "timestamp":int(time.time())
    }

    return event

