from app.services.tariff_service import calculate_cost


def test_calculate_cost():
    usage = 2

    cost = calculate_cost(usage)

    assert cost == 16