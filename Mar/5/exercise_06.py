list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

common = []
for num in list_a:
    if num in list_b:
        # Anti-pattern: 'in list_b' is a hidden loop.
        # This creates O(n^2) Quadratic time.
        common.append(num)

set_b = set(list_b)

fast_common = []
for num in list_a:
    if num in set_b:
        # Pythonic: 'in set_b' takes exactly 1 step.
        # Time drops strictly to O(n) Linear time.
        fast_common.append(num)