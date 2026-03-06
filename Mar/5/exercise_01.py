word = "Python"

sliced = word[::2]
# Returns "Pto". The step adds exactly 2 to the index
#0 ('P'), then 2 ('t'), then 4 ('o').

for char in sliced:
    # Iteration. Pulls each character out sequentially

    if char == "t":
        # Guard Clause inside the iteration.
        continue
        # Halts this specific cycle and jumps back
        # to the top for the next character.

    processed = char + "_done"
    # This line only executes if the Guard fails.