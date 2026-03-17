# The "Sovereign" vertical wrap for descriptive comprehesions:

results = [
    currency_rate
    for currency_rate in raw_payload_list
    if isinstance(currency_rate, float)
]