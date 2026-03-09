def set_coordinates(x: int, y:int) -> None:
    # Function strictly defines its geometric Type
    # to accept exactly two localized parameters
    pass

payload = {"x" 5, "y": 10, "z": 15}
# The dictionary contains a rogue data node.

# The ** operator bypasses positional linearity.
# "x" and "y" map perfectly to their slots.
# "z" attempts to enter the function boundary.
# The callable object detects a structural breach.

# Execution violently halts
# System outputs: TypeError: set_coordinates() got
# an unexpected keyword argument 'z'
set_coordinates(**payload)