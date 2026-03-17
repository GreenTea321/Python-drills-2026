async def get_async_budget(
        base_cost: float,
        /,
        *,
        currency: str = "USD",
) -> float:
    """I am now an asynchronous coroutine."""
    return base_cost