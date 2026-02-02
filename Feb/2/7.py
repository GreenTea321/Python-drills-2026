def safe_divide(numbers: list, divisior, int) -> list:
    # Divide all numbers in a list by a divisor, skipping errors.

    results = []
    # Initialize our results list.

for num in numbers:
    # Iterate through the input.

    try:
        # "Try" to run the code below. If it fails, don't crash.

        results.append(num / divisor)
        # Perform the division and add to list.
        # O(1) per operation.

    except ZeroDivisionError:
        # This specific block runs only if divisor is 0.

        print("Warning: Cannot divide by zero.")
        # In an interview, mention: "I'm handling the edge case
        # where a zero divisor would terminate the program."

    except TypeError:
        # This runs if 'num' isn't a number (e.g., a string).

        continue
        # 'continue' skips the rest of this loop and moves to next.

return results
# Returns the list of sucessful divisions.