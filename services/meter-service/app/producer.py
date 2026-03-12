import json
from kafka import KafkaProducer
from config.settings import KAFKA_BOOTSTRAP_SERVERS

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def send_meter_event(event):
    producer.send("meter_usage", event)
    producer.flush()

    print(f"Sent event: {event}")

