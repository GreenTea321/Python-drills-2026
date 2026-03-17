import asyncio

async def clean_and_sort(
        raw_data: list[float | None | str],
) -> list[float]:
    """Filters for floats and sorts them decending."""
    # List Comprehesion to filter out non floats
    results = [floats for item in raw_data if isinstance(item, float)]
    
    # Take results and sort them in descending order.
    sorted_results = sorted(results, reverse=True)

    # Return the list of floats that have been sorted.
    return sorted_results