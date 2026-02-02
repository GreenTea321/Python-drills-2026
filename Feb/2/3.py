def get_long_words(word_list: list) -> list:
    # Filter a list to keep only words longer than 3 characters.

    filtered = [word for word in word_list if len(word) > 3]
    # This is a List Comprehension. It's high speed "shorthand."
    # Logic: "Give me 'word' for every 'word' in 'word_list'
    # BUT only 'if' the length of that word' is greater than 3."

    return filtered
    # Time Complexity: O(n) because we check every word once.
    # Space Complexity: O(m) where m is the number of words kept


def get_long_words_long_form(word_list: list) -> list:
    # Manual appraoch to filtering a list

    result = []
    # Initialize an empty list (O(1) space.

    for word in word_list:
        # Loop through every item. O(n) time.

        if len(word) > 3:
            # Check the condition (length greater than 3).

            result.append(word)
            #.append() adds 'word' to the end of the 'result' list.
            # this is how we build lists piece-by-piece in a loop.

    return result
    # Return the final filtered list.