import asyncio

async def resilient_fetch(base: str, target, str) -> list:
    # I will crash if one task fails
    task1 = api.get_rate(base)
    task2 = api.get_rate(target)

    # Logic Bomb: If task1 fails, the whole program halts here
    return await asyncio.gather(task1, task2, return_exceptions=True)