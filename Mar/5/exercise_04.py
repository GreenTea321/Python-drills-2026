player_data = {"health": 100, "status": "active"}
# Dictionaries map keys to values for O(1) lookups

hp = player_data["health"]
# Direct access. Throws KeyError if key is missing.

meter = player_data.get("meter", 0)
# .get() acts as an inline Guard Clause.
# Returns 0 if "meter" is not found. No crash.