def get_player_stat(game_data: dict, name:str, stat:str) -> int:
    # Dig into a nested dictionary to find a specfic player's stat.

    # 1. THE SAFETY SHIELD
    if name not in game_data:
        return 0
        # If the player doesn't exist, return a default value of 0.

    player_info = game_data[name]
    # 'player_info' is now a dictionary itself (the nested one).

    # 2. THE NESTED CHECK
    result = player_info.get(stat, 0)
    # Use .get() on the inner dictionary to safely find the stat.
    # If 'power' exists, it returns it. If not, it returns 0.

    return result
    # Time Complexity: O(1) because both are hash map lookups.
    # Space Complexity: O(1) as we aren't creating new data structures.

