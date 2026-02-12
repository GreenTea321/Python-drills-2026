def get_player_hp(data_packets: list, target_name: str) -> int:
    #1. The loop iterates through a list of dictionaries.
    for packet in data_packets:

        # 2. Check if the 'name' key in this drawer matches our target.
        if packet.get("name") == target_name:

            # 3. Return the HP associated with that specific packet.
            return packet.get("hp", 0)

    # 4. The Final Safety Shield
    return -1