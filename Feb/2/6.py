def is_list_sorted(nums: list) -> bool:
    # Check is a list of numbers is in ascending order.

    for i in range(1, len(nums)):
        # We start at index 1 (The second item)
        # We need the "current" and previous" to ccompare.

        if nums[i] < nums[i - 1]:
            # If the current number is smaller than the one before it...

            return False
            # ...the list is NOT sorted. We "Fail fast" and exit.
            # Time Complexity:O(n) worst case. but could be O(1).

    return True
    # If the loop finishes without returning False, It's sorted.
    # Space Complexity: O(1) because no new data is created.