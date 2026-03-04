frames = [4, 5, 8, 12]

fast_frames = [f * 2 for f in frames if f < 10]
# Architecture: [expression for item in iterable if condition]
# Mechanism: Allocates the array size directly in C rather than
# dynamically resizing via. append() per iteration.
# Big O: O(n) time, O(k) space (k = elements passing the Guard).

inputs = ['A', 'B']
states = ['Stand,' 'Crouch']

moves = [s + '_' + i for s in states for i in inputs]
# Logic: Left-to-right evaluation matches nested loop hierarchy.
# Outer loop is 'states', inner loop is 'inputs'.
# Generates a Cartesian product without deep indentation.

matrix = [[1, 2], [3, 4]]

flat = [num for row in matrix for num in row]
# Execution sequence:
# 1. for row in matrix (Access outer block)
# 2. for num in row (acccess inner element)
# 3. num (Evaluate expression and yield)