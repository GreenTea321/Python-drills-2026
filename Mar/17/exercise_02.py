import asyncio
import time

async def blocked_latency(duration: float) -> float:
    """I have a hidden logic bomb inside me"""
    start_time = time.perf_counter()

    # Task 1: Asynchronous
    task1 = asyncio.sleep(duration)

    # Task 2: Synchronous (The Logic Bomb!)
    task2 = asyncio.sleep(duration)

    await asyncio.gather(
        task1,
        task2,
    )

    return time.perf_counter() - start_time

