def sum_even_numbers(numbers: list) -> int:
    total = 0
    # Init accumultor
    # Must be defined before += usage.

    for num in numbers:
        # Iterates over values directly, not index.
        # Use Enumerate if index is needed.

        if num % 2 == 0:
            # Modulo operator %. Returns remainder.
            # 0 Means divisible by 2 (even).

            total += num
            # In-place add. Creates new int object.
            # Python ints are immutable.

    return total
    # Returns result.
    # Implicitly returns None if missing.

def count_vowels(text:str) -> int:
    vowels = "aeiouAEIOU"
    # String used as collection.
    # Case-senseitive loopup.

    count = 0
    # Initialize counter integer.

    for char in text:
        # Strings are iteratble sequences.

        if char in vowels:
            # The 'in' keyword checks membership.
            # Scans 'vowels' to see if 'char' exists

            count += 1
            # Increment count.

        return count
        # Returns final integer count.

def reverse_words(sentence: str) -> str:
    words = sentence.split()
    # String method.
    # Splits by whitespace into a list of strings.

    reversed_list = words[::-1]
    # List slicing syntax [start:stop:step].
    # Step of -1 creates a reversed COPY.

    result = " ".join(reversed_list)
    # String method.
    # " " acts as the glue/seperator.

    return result
    # Returns the new string.














            