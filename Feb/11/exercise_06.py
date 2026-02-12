def sum_scores(scores: dict) -> int:
    total = 0
    # Init accumulator.

    for score in scores.values()
        #.values() method
        # Returns a view of ONLY the values (10, 20).
        # Ignores keys entirely.

        total += score
        # Adds the integer values directly.

    return total
    # Returns 30.

def format_roster(players: dict) -> list:
    # Input: {'Alice': 10, 'Bob': 20}
    formatted = []
    # Init empty list for results.

    for name, score in players.items():
        # .items() method. CRITICAL for interviews.
        # Returns a Tuple of (key, value) for each entry.
        # We "unpack" them into 'name' and 'score' variables instantly.

        entry = f"{name}: {score}"
        # f-string formatting.
        # Injects variables directly into the string.

        formatted.append(entry)
        # adds "Alice: 10" to list.

    return formatted
    # returns list of strings.

def find_position(racers: list) -> list:
    # Input: ["Mario", "Luigi", "Peach"]
    results = []

    for index, racer in enumerate(racers):
        # enumerate() function.
        # Returns a tuple: (index, item).
        # (0, "Mario"), (1, "Luigi")...

        rank = index + 1
        # Convert 0-based index to 1-based rank.

        entry = f"Rank {rank}: {racer}"

        results.append(entry)

    return results

























