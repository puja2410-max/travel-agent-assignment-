def replan_on_delay(itinerary, delay_hours):
    # simple strategy: find nearest alternative or propose hotel stay
    if delay_hours >= 6:
        return [ { 'option': 'overnight_hotel', 'cost_delta': 2000 }, { 'option': 'alternate_flight', 'cost_delta': 5000 } ]
    return []
