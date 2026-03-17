import asyncio
async def fetch_and_clear(
        base: str,
        target: str,
) -> list[float]:
    """Fetches two rates and cleans the results."""
    # 1. Start the 'Futures' (tickets) for both rates
    t1 = api.get_rate(base)
    t2 = api.get_rate(target)

    # 2. Gather both, ensuring exceptions are returned as objects
    results = await asyncio.gather(t1, t2, return_exceptions=True)

    # 3. Use your 'Algorithmic Factory to return only the floats
    return [item for item in results if isinstance(item, float)]