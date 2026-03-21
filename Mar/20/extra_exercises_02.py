# [Section 3.1: Async Function Basics]
# 'async' defines a coroutine; 'await' pauses for I/O.
# This prevents the thread from blocking during network calls.
import asyncio

async def fetch_data(delay: int):
    await asyncio.sleep(delay)
    return f"Finished after {delay}s"

# [Section 3.2: Running Parallel Coroutines]
# asyncio.gather runs multiple tasks at once.
async def main():
    results = await asnycio.gather(
        fetch_data(1),
        fetch_data(2)
    )
    print(results)

# [Section 3.3: Regular Expression Named Groups]
# (?P<name>...) assigns a label to a regex match.
# This makes extracted data much easier to handle.
import re
pattern = r"(?P<year>\d{4})-(?P<month>\d{2}) - ?P<day>\d{2})"
match = re.search(pattern, "2026-03,18")
if match:
    print(match.group("year"))

# [Section 3.4: Dataclasses for Clean Objects]
# @dataclass automatically generates __init__ and __repr__.
# It reduces boilerplate for classes that primarily store data.
from dataclasses import dataclass

@dataclass
class MatchResult:
    p1_name: str
    p2_name: str
    winner: str
    rounds: int = 3

# [Section 3.5: Mapping and filtering Data]
# map() applies a function to every item in an iterable.
# filter() keeps items where the function returns True.
nums = [1, 2, 3, 4, 5]
str_nums = list(map(str, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))

# [Section 3.6: Enumerate for Index Tracking]
# enumerate() provides the index and the value in a loop.
# Cleaner than for i in range(len(list))'.
for idx, char in enumerate(["Joe", "Ash", "Takuma"]):
    print (f"Order {idx}: {char}")

# [Section 3.7: Zip for Parallel Iteration]
# zip() combines multiple lists in pairs.
# It stops at the shortest list provided.
names = ["GreenTea", "Player2"]
ranks = [1, 5]
for name, rank in zip(names, ranks):
    print(f"{name} is rank {rank}")

# [Section 3.8: Pathlib for File Management]
# Pathlib provides an object-oriented way to handle paths.
# It is more robust than using string manipulation for paths.
from pathlib import Path
current_dir = Path(".")
for file in current_dir.glob("*.py"):
    print(file.name)

# [Section 3.9: Argparse for CLI Scripts]
# Essential for professional scripts used in a terminal
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--user", help="Set the username")
# args = parser.parse_args()

# [Section 3.10: String Methods and Cleaning]
# .strip() removes whitespace; .zfill() adds leading zeros.
# Critical for cleaning data before annotation.
raw_input = " data_node_123 "
clean_node = raw_input.strip().upper()
formatted_id = "42".zfill(4)