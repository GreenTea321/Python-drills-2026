def calculate_damage(base: int, multiplier: int, bonus: int) -> int:
    return (base * multiplier) + bonus
    # The function demands exactly three integers.

stats = [50, 2]
# The array provides only two data nodes.

failed_damage = calculate_damage(*stats)
# The asterisk unpacks 50 into 'base, and 2 into 'multiplier'.
# The 'bonus' parameter receives nothing.
# The system violently halts, raising a TypeError.