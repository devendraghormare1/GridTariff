from app.services.aggregation_service import aggregate_usage
from app.model.meter_event import MeterEvent


def test_aggregate_usage():
    event = MeterEvent("MTR001", 2.5, 1234556)

    usage = aggregate_usage(event)

    assert usage == 2.5

    