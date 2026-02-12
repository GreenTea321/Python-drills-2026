def get_average_score(player_list: list) -> float:
    #1. THE SAFETY SHIELD
    if not player_list:
        return 0.0
        # Prevents ZeroDivisionError if the list is empty.

    total_points = 0
    valid_count = 0

    for player in player_list:
        #2. THE SAFE RETRIEVAL
        score = player.get("score")
        # Returns None if "score" is missing.

        if score is not None:
            # Only process if data exists.
            total_points += score
            valid_count += 1
            # We only increment count for actual data points.

    # 3. FINAL LOGIC CHECK
    if valid_count == 0:
        return 0.0

    return total_points / valid_count
    # Time complexity: O(n) - we touch every player once 
    # Space Complexity: O(1) - We only store two integers