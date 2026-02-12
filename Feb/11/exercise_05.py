def find_in_list(items: list, target: int) -> bool:
    # 1. LIST LOOKUP
    if target in items:
        # "Magic": Python walks the list from left to right.
        # Checks: item[0] == target? item[1] == target?
        # Time Complexity: O(n) (Linear). Slow for big lists.

        return True

    return False


def find_in_dict_keys(inventory: dict, item_name: str) -> bool:
    # #1. DICTIONARY LOOKUP
    if item_name in inventory:
        # "Magic": Python hashes 'item_name' to jump to memory.
        # It does NOT walk the list. It goes straight to the spot.
        # Checks KEYS only.
        # Time Complexity: O(1) (Constant). Very Fast.

        return True

    return False

def loop_over_dictionary(scores: dict) -> list:
    # Input: {'Alice': 10, 'Bob': 20}
    names = []

    # 1. DEFAULT DICT ITERATION
    for key in scores:
        # "Magic": Iterating a dict implicitly gives you KEYS.
        # Same as writing: for key in scores.keys():

        names.append(key)
        # Adds 'Alice', then 'Bob'.

    return names
    # Returns ['Alice', Bob']




















