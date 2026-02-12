def get_average_score(player_list: list) -> float:
    if not player_list:
        return 0.0
        #1. THE SAFETY SHIELD
        # Prevents ZeroDivisionError if the list is empty.

    total_points = 0
    valid_count = 0

    for player in player_list:
        
        score = player.get("score")
        
        #2. THE SAFE RETRIEVAL
        # Returns None if "score" is missing.

        if score is not None:
            # Only process if data exists.
            total_points += score
            valid_count += 1
            # We only increment count for actual data points.

    
    if valid_count == 0:
        return 0.0    
    # 3. FINAL LOGIC CHECK

    return total_points / valid_count
    # Time complexity: O(n) - we touch every player once 
    # Space Complexity: O(1) - We only store two integers