async def fetch_exchange_rate(
        currency: str,
        /,
) -> float:
    """Fetches the rage from a remote API."""
    # We use await here to 'pause' until the data arrives
    rate = await api.get_rate(currency)
    return rate