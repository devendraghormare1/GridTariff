
from config.settings import TARIFF_RATE

def calculate_cost(usage_kwh):
    return round(usage_kwh * TARIFF_RATE, 2)

