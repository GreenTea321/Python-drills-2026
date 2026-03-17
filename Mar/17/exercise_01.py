import asyncio
import time

async def model_latency(
        duration: float,
        /,
) -> float:
    """Models API latency using parallel sleeps."""
    start_time = time.perf_counter()

    # We gather two identical 'sleep' coroutines
    await asyncio.gather(
        asyncio.sleep(duration),
        asyncio.sleep(duration),
    )

    total_time = time.perf_counter() - start_time
    return total_time

if __name__ == "__main__":
    # We use asyncio.run to 'kick-start' the event loop
    result = asyncio.run(model_latency(2.0))
    print(f"Total parallel time: {result:2f}s")