def configure_player(name: str, speed: int) -> str:
    return f"Player {name} moves at {speed}."

player_data = {"name": Rolento, "speed": 100}
# The dictionary keys perfectly mirror the target parameters.

configured_status = configure_player(**player_data)
# The double-asterisk operator (**) detonates the dictionary.
# "Rolento" bypasses position and maps directly to 'name'.
# 100 bypasses position and maps directly to 'speed'.

print(configured_status)
# Successfully outputs the formatted string.