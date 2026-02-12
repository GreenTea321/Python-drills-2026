def get_team_total_health(roster: dict, team_name: str) -> int:
    # Calculate total health for a specific team in the tournament

    if team_name not in roster:
        return 0
        # Guard clause ensures we don't try to loop over a missing team

    total_health = 0
    team_members = roster[team_name]
    # 'team_members' is now a dict of characters (e.g. {"Ralf": {..}}).

    for member_name in team_members:
        # We iterate through the keys (names) of the team dictionary.

        character_stats = team_members[member_name]
        # This gets the inner dict: {"health": 120, "power": 130}