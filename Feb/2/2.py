def count_with_get(text: str) -> dict:
    # Function to count chars without using explicit if-else checks.

    counts = {}
    # Initialize our O(1) lookup table (dictionary).
    
    for char in text:
        # Iterate through the string. O(n) time complexity.

        counts[char] = counts.get(char, 0) + 1
        # This one line handles both existence check and incrementing
        # .get(key, default) returns the value if it exists.
        # If 'char' is NOT in dict, it returns 0 (our default).
        # Then we add 1 to that result and save it back to 'char'.

    return counts
    # Returns the populated dictionary.
    # This is preferred in interview for its readability and brevity.