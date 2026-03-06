try:
    data = int("not_a_number")
except ValueError:
    # Python uses ' except' instead of 'catch' to
    # intercept the error and keep the program alive.

    data = 0

action = "jump"

match action:
    # Added in Python 3.10. Structural Pattern
    # Matching flattens deep if/then structures.

    case "attack":
        damage = 10

    case "jump":
        height = 5
        # Executes cleanly without needing an 'elif'.

    case _:
        status = "idle"
        # The '_' acts as a wildcard, catching
        # anything that did not match above.