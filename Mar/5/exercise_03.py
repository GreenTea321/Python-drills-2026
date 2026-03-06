chars = [c + "_done" for c in "Pto"]
# List comprehensions establish a strictly local scope.
# The variable 'c' does not leak into the wider state.

def process_string(text: str) -> list:
    # Functions create an impentrable scope boundary.

    result = []
    for char in text:
        result.append(char)

    return result
    # 'result' and 'char' are destroyed after the return.