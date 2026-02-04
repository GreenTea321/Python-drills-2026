def get_unique_characters(char_list: list) -> set:
    # Extract unique names from a list that might have duplicates.

    if not char_list:
        return set()
        # Note: We use 'set()' for an empty set, not '{}'
        # (because '{}' creates an empty dictionary!).

    unique_chars = set(char_list)
    # This is an O(n) operation that automtiaclly removes duplicates.
    # A 'set' only allows one of each item.

    # Interview Logic: "I'm using a set here because it provides
    # O(1) average time complexity for memebership checks and
    # natively handles duplicate removal."

    return unique_chars
    # Space Complexity: O(u) where u is the number of unique items.         # Time Complexity: O(n) for the set conversion            .