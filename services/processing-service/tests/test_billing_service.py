from app.services.billing_service import generate_billing_record


def test_generate_billing_record():
    record = generate_billing_record("MTR001", 2.0, 16)

    assert record["meter_id"] == "MTR001"
    assert record["usage_kwh"] == 2.0
    assert record["cost"] == 16
    