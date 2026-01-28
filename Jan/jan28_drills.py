def get_user_rank(rank_map, user_id):
    rank = rank_map.get(user_id, "Unranked")
    # Syntax: .get() is a dictionary method; it takes(key, default_value).
    # Logic: It attempts to find the key. If the key is missing, it returns
    # the second argument ("Unranked") instead of crashing the program.
    # Performance: O(1) constant time; safer than using rank_map[user_id].

    return rank.upper()
    # Syntax: .upper() is a string method.
    # Logic: Converts the result to all caps (e.g., "GOLD" or "UNRANKED").
    # Performance: O(m) where m is the length of the string

# testing again





Questions: can you tell me about m in  O(m) where m is the length of the string?