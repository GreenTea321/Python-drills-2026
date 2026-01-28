def find_common_players(team_a, team_b):
    set_ a = set(team_a)
    # Syntax: set() constructor. Logic: Convert list to hash table.
    # Time: O(n) to hash team_a. Space: O(n) to store the set.

    common = [player for player in team_b if player in set_a]
    # Syntax: List comprehension with a conditional check.
    # Logic: Keep name only if it exists in the first set.
    # Time: O(m) because 'in set_a' is a constant O(1) lookup.
    # Space: O(k) where k is the number of common items.
    # Use Case: Finding shared data between two large databases.

    return common