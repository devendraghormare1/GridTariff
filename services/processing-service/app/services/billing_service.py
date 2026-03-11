
def generate_billing_record(meter_id, usage, cost):
    billing_record = {
        "meter_id": meter_id,
        "usage_kwh": usage,
        "cost": cost
    }

    return billing_record

