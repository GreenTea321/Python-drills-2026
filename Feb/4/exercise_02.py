def calculate_team_power(roster: dict, team_name: str) -> int:
    # Sum the 'power' stats for a team using the .items() method.

    if team_name not in roster:
        return 0

    total_power = 0
    team_dict = roster[team_name]

    for name, stats in team_dict.items():
        # .items() gives us BOTH the Key and the Value at the same time.
        # 'name' = "Leona" (th key)
        # 'stats' = {"health": 100, "power": 150} (the Value)