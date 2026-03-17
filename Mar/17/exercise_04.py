async def process_results(
        results: list[float | Exception],
        /,
) -> list[float]
    """Filters out any exceptions and returns only floats"""
    # Use your 'Algorithmic' brain to filter the list here
    return [item for item in results if isinstance(item, float)]