def get_move_data(move_set, move_name):
    data = move_set.get(move_name,"N/A")
    # Syntax: .get() method with a fallback default value.
    # Logic: Returns "N/A" if the key move_name is missing.
    # Time: O(1). Space: O(1).
    # Use Case: Handling user input where they might type a wrong key.

    return data