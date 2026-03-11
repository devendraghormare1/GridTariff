import json
from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def send_meter_event(event):
    producer.send("meter_usage", event)
    producer.flush()

    print(f"Sent event: {event}")

