def configure_player(name: str, speed: int) -> str:
    return f"Player {name} moves at {speed}."
    # The target function strictly requires 'name' and 'speed'.

player_data = {"Character_name": "Rolento", "speed": 100}
# The dictionary contains a key ('character_name') that does
# not exist in the function's parameter signature.

configured_status = configure_player(**player_data)
# The double-asterisk operator attempts the injection.
# The 'speed' maps successfully.
# 'character_name' finds no matching slot and violently halts the sequence.
# The system raises: TypeError: configure_player() got an unexpected keyword argument 'character_name'

