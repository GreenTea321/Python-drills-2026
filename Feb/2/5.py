def double_in_place(numbers: list) -> None:
    # Modify every number in the list by doubling it.
    # -> None means this function returns nothing; it modifies the input.

    for i, val in enumerate(numbers):
        # enumerate() gives us the index (i) and the current value (val)
        # This is the standard way to get a "counter" in a loop

    numbers[i] = val * 2
    # We reach into the original list at index 'i' and overwrite it.
    # Space Complexity: O(1) because we don't create a new list.
    # Time Complexity: O(n) because we visit each elemment once.

# No return statement needed; the original list is now changed.