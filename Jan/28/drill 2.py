def check_username(user_dict, name):
    # Syntax: 'in' keywords checks keys in a dictionary.
    # Logic: Verifies if 'name' exists before we try to read it.
    # Performance: O(1) constant time; it doesn't scan every entry.
    if name in user_dict:

        # Syntax: Accessing the value using the key in brackets [].
        # Logic: Pulls the specific data associated with that name.
        return user_dict[name]

    # Logic: Fallback if name is missing; prevents a KeyError crash.
    return "Not Found"