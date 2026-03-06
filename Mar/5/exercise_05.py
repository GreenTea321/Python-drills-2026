def linear_search(roster, target):
    for fighter in roster:
        if fighter == target:
            return True
        
    return False
    # O(n) Linear time. It checks index 0, then 1,
    # then 2. The time scales directly with the size
    # of the sequence.

def constant_lookup(character_map, target):
    return character_map.get(target)
    # O(1) Constant Time. Python mathematically hashes
    # the string into a direct memory address. It
    # jumps there instantly, skipping the manual search.