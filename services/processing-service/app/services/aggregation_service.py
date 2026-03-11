def aggregate_usage(event):
    """
    For now we simple pass usage through.
    Later we can aggregate hourly/daily usage.
    """

    return event.usage_kwh


