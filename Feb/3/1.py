def map_results(data_list: list) -> dict:
    # Convert a list of (name, score) tuples into a dictionary.

    #1. The Safety SHIELD
    if not data_list:
        return {}
        # Guard clause: if data is None or empty return an empty dict.
        # This prevents O(n) work on an empty object.

    result_map = {}
    # Initialize our hash map. O(1) space for the reference.

    for name, score in data_list:
    # TUPLE UNPACKING: We extract 'name' and 'score' in one go.
    # This is more readable than using data_list[0][0].

        try:
            result_map[name] = int(score)
            # We cast to 'int' just in case the data came in as a string.
            # Time Complexity: O(n) to iterate through the list.

        except (ValueError, TypeError):
            # If 'score' isn't a valid number, we skip this entry.
            continue
            # This ensures the dictionary only contains valid data.

    return result_map
    # Space Complexity: O(k) where k is the number of unique names.