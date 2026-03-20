# [Section 2.1: Advanced Type Hinting]
# Using 'Union' allows a variable to be one of multiple typpes.
# Optional[T]' is shorthand for 'Union[T, None]'.
from typing import Union, List, Optional

def process_id(uid: Union[int, str]) -> str:
    return str(uid).strip().zfill(5)

# [Section 2.2: Positional-Only and Keyword-Only Arguments]
# Arguments before '/' must be positional.
# Arguments after '*' must be keyword-based
def configure_system(mode, /, *, debug=False, retries=3):
    print(f"mode: {mode}, Debug: {debug}")

# [Section 2.3: F-Strings with Formatting Specifiers]
# .2f rounds a float to two decimal places.
# >10 right-aligns text within a 10-character block.
pi = 3.14159
name = "GreenTea"
print(f"Score: {pi:.2f} | User: {name:>10}")

# [Section 2.4: Set Comprehensions for Unique Filtering]
# Sets automatically discard duplicate entries.
# Useful for finding unique characters in a data stream
raw_data = ["Ash", "Joe", "Takuma", "Joe"]
unique_chars = {name.upper} for name in raw_data}
    
# [Section 2.5: The 'itertools.chain' for Flat Iteration]
# chain combines multiple iterables without creating a new list.
import itertools
list_a = [1, 2, 3]
list_b = [4, 5, 6]
for x in itertools.chain(list_a, list_b):
    print(x)

# [Section 2.6: Custom Context Managers (Decorator Style)]
# Allows you to use the 'with' syntax for custom logic.
from contextlib import contextmanager 

@contextmanager
def timer_context():
    import time
    start = time.time()
    yield
    print(f"Elapsed: {time.time() - start}")

# [Section 2.7: Class Structure with __repr__]
# __repr__ defines the developer-friendly string representation.
# This is vital for debugging complex object states.
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def __repr__(self)
        return f"Character(name='{self.name}, hp = {self.health})"
    
# [Section 2.8: Property Decorators for Managed Attributes]
# Use @property to turn a method into a read-only attribute.
# Use @setter to validate data before updating an attribute.
class GameSession:
    def __init__(self, score):
        self._score = score

        @property
        def score(self):
            return self._score
        
        @score.setter
        def score(self, value):
            if value < 0:
                raise ValueError("Score cannot be negative")
            self.score = value

# [Section 2.9: Multiple Exception Handling]
# Catching specific errors prevents the program from crashing.
# 'else' runs if no error occurred; 'finally' runs always.
try:
    result = 10 / int("5")
except (valueError) ZeroDivisionError) as e:
    print f("Error: {e}")
else:
    print(f"Result is {result}")
finally:
    print("Cleanup complete.")

# [Section 2.10: Variable Scoping and 'nonlocal']
# 'nonlocal' allows you to modify a variable in the outer scope.
# This is the basis for creating stateful closures.
def create_counter():
    count = 0 
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
