# The tuple binds three permanent memory pointers.
immutable_shell = (1, 2, [3, 4])

# We cannot do immutable_shell[0] = 99.
# That breaks the Tuple's static pointer rule.

# But we can mutate the list residing at index 2.
immutable_shell[2].append(5)

# The pointer remains static, the payload grew.

# The pointer remains static, but the payload grew
print(immutable_shell)
# Outputs: (1, 2, [3, 4, 5])

