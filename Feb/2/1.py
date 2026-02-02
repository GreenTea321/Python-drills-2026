def get_charfrequency(text: str) -> dict:
    #Function signature with type hinting.
    # Input: 'text' string. Output: Dictionary mapping chars to counts.

    freq_map = {}
    # Initialize empty dictionary. O(1) space complexity initially.
    # This will serve as our hash map for constant time lookups.

    for char in text:
        # Loop through every character in the string.
        # This gaurantees O(n) Time Complexity where n is string length.

        if char in freq_map:
            # Check if key exists. Hash map lookups are o(1) on average.

            freq_map[char] += 1
            # Increment existing count.
            # Essential for tracking accumulation without overwriting.

        else:
            freq_map[char] = 1
            # Initialize the count for a new unique character.
            # This handles the "first encounter" edge case.

    return freq_map
    # Return the populated hash map.
    # Total Space Complexity: O(k) where k is number of unique chars.