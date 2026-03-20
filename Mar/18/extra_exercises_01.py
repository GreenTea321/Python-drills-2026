[Section 1.1: Lazy Evaluation and Memory Management]
# Generator expressions save RAM by not creating a full list in memory
data = range(1000000)
squared_gen = (n ** 2 for n in data if n % 2 == 0)

# The 'next' function retrieves the next item from the generator.
# This prevents loading all 1,000,000 items at once.
first_val = next(squared_gen)
second_val = next(squared_gen)

# [Section 1.2: Dictionary safety and the .get() method]
# Using .get() prevents KeyError when a key is missing
user scores = {"GreenTea": 95, "Player2": 88}
score = user_scores.get("Guest", 0)

# [Section 1.3: Dictionary Comprehensions with logic]
# This creates a map of even numbers to their cubes.
# Syntactic pattern: {key: value for item in iterable if condition}
cube_map{
    x: x**3
    for x in range(10)
    if x % 2 == 0
}

# [Section 1.4: Tuple Unpacking and Placeholder Variables]
# Use '_' to ignore values you don't need during unpacking.
# This keeps the namespace clean and signals intent to other devs
player_data = ("GreenTea", 32, "New York", "KOF-XIII")
username, _, _, main_game = player_data

# [Section 1.5]: List Slicing and Step Paramters]
# Syntax: list[start:stop:step]
# A step of -1 is the standard way to reverse a sequence.
numbers = [1, 2, 3, 4, 5, 6]
reversed_evens = numbers[::-2]

# [Section 1.6: The 'with' Statement for File I/O]
# This ensures the file is closed even if an error occurs.
# Professionals always use 'with' to avoid file descriptor leaks.
with open("log.txt", "a") as f:
    f.write(f"Log entry: {username} - {score}\n")

# [Section 1.7: Lambda Functions for Inline Transformation]
# Lambdas are anonymous functions used for short-lived logic.
# Here, we sort a list of tuples by the second element.
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda x: x[1])

# [Section 1.8: Any and All for Boolean Aggregation]
# 'all' returns True if every element is True.
# 'any' returns True if at least one element is true.
requirements = [True, True, False]
is_valid = all(requirements)
has_one_pass = any(requirements)

# [Section 1.9: NamedTuples for Readable Data Structures]
# NamedTuples act like classes but are memory-efficient like tuples.
from collections import namedtuple
Player = namedtuple('Player', ['name', 'rank', 'main'])
p1 = Player('GreenTea', 1, 'Joe Higashi')

# [Section 1.10: Defaultdict for Automatic Initialization]
# Avoids 'if key in dict' checks by providing a default value.
from collections import defaultdict
counts = defaultdict(int)
for word in ["kof", "kof", "sf"]:
    counts[word] += 1