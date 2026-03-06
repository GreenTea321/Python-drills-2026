import sys

linear_array = [1, 2, 3, 4, 5]
# Lists pack data tightly. CPU works harder to search,
# but the overall RAM footprint is minimized.

hash_map = {1, 2, 3, 4, 5}
# Sets spread data out to avoid mathematical collisions.
# CPU finds item instantly, but RAM usage doubles.

array_size = sys.getsizeof(linear_array)
# Evaluates to roughly 104 bytes in memory.

set_size = sys.getsizeof(hash_map)
# Evaluates to roughly 216 bytes in memory.