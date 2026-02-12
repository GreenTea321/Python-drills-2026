# Assume d = {"Kyo": 100, "Iori": 95}

# 1. THE KEYS (Default)
for name in d:
    print(name)
    # Output: Kyo, Iori
    # Use this when you only care about labels.

# 2. THE VALUES
for score in d.values():
    print(score)
    # Output: 100, 95
    # Use this when you don't care who the players are.

# 3. THE ITEMS(The "Librarian")
for name, score in d.items():
    print(name, score)
    # Output: Kyo 100, Iori 95
    # This is "Unpacking". PYthon takes the pair and splits it.
    # 'name' gets the key, 'score' gets the value.