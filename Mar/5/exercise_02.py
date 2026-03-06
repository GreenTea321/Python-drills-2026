results = []
# Explicitly creating an empty list first.

for char in "Pto":
    if char == "t'":
        continue

    results.append(char + "_done")
    # Mutates the list in place, adding the
    # string to the end of the sequence.