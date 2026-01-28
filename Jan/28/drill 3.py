def reset_lobby(players):
    # Syntax: .clear() is a list method.
    # Logic: Remove all items but keeps the same object in memory.
    # Performance: O(n) to remove 'n' items from the list.
    players.clear()

    #Syntax: len() returns the integer count of items.
    # Logic: Confirming the list is now empty(0).
    return len(players)