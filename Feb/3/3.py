def filter_banned_players(players: list, banned_set: set) -> list
    # Return a list of players who are not in a the banned set.

    #1. THE SAFETY SHIELD
    if not players:
        return []

    allowed_players = []
    # Using a list because the of players might matter.

    for player in players:
        # Standard I(n) iteration.

        if player not in banned_set:
            # This 'in' check is O(1) because banned_set is a SET.
            # If banned_set was a list, this would be O(n) making the
            # total function O(n^2) - a huge interview mistake!)

            allowed_players.append(player)
            # Add the clean data to our results.

    return allowed_players
    # Final result is a "clean" lsit.