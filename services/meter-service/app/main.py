from apscheduler.schedulers.blocking import BlockingScheduler
from app.meter_generator import generate_meter_event
from app.producer import send_meter_event


scheduler = BlockingScheduler()

def produce_event():
    event = generate_meter_event()
    send_meter_event(event)


scheduler.add_job(produce_event, "interval", seconds=5)

print("Meter service started....")

scheduler.start()

