import json
from kafka import KafkaConsumer
from app.model.meter_event import MeterEvent
from app.services.aggregation_service import aggregate_usage
from app.services.tariff_service import calculate_cost
from app.services.billing_service import generate_billing_record   
from app.repositories.redis_repository import store_meter_data
from config.settings import KAFKA_BOOTSTRAP_SERVERS

consumer = KafkaConsumer(
    "meter_usage",
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest",
    group_id="processing-group"
)

def start_consumer():
    print("Processing service started...")

    for message in consumer:
        data = message.value

        event = MeterEvent(
            data["meter_id"],
            data["usage_kwh"],
            data["timestamp"]
        )

        usage = aggregate_usage(event)

        cost = calculate_cost(usage)

        billing_record = generate_billing_record(event.meter_id, usage, cost)

        store_meter_data(event.meter_id, billing_record)

        print(f"Processed {billing_record}")


