def boost_stats(stats):
    for i in range(len(stats)):
        # Syntax: range(len()) generates indices 0 to N-1.
        # Time: O(n). Space: O(1) as we don't create a new list.

            stats[i] = stats[i] * 2
            # Logic: Multiply each integer in the original list by 2.
            # Use Case: Mobile or embedded apps with very limited RAM.

     return stats
