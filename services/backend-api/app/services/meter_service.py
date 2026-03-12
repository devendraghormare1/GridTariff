from app.repositories.redis_repository import get_meter_data, get_all_meters

def fetch_meter_data(meter_id):
    return get_meter_data(meter_id)

def fetch_all_meters():
    return get_all_meters()
