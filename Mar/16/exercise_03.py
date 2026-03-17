import asyncio

async def get_multiple_rates(
        base: str,
        target: str,
) -> list[float]:
    """Fetches two rates in parallel."""
    # We call the functions but don't 'await' them yet
    task1 = api.get_rate(base)
    task2 = api.get_rate(target)

    # We await both at the same time
    return await asyncio.gather(task1, task2)
