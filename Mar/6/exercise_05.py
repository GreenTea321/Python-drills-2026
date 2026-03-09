def calculate_damage(base: int, multiplier: int, bonus: int) -> int:
    # A standard function expecting three distinct integers.
    return (base * multiplier) + bonus

stats = [50, 2, 10]

# INFERIOR METHOD: Manual index extraction.
# This introduces visual noise and structural fragility.
slow_damage = calculate_damage(stats[0], stats[1], stats[2])

# SUPERIOR METHOD: The unpacking operator (*).
# The asterisk detonates the list boundary, injecting
# 50, 2, and 10 directly into the matching parameter slots.
fast_damage = calculate_damage(*stats)

print(fast_damage)