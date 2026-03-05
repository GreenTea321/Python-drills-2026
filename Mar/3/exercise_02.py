word = "crash"

copy_one = word[:]
# Slices from absolute start to absolute end.
# Creates a shallow copy of the entire string.

copy_two = word[::]
# The third slot is the 'step' argument.
# Defaults to 1. Also creates a full copy.

reversed_word = word[::-1]
# A negative step iterates backwards.
# Structurally reverses the string to 'hsarc'
