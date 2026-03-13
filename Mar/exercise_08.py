# The "Sovereign" way to handle optional lists:
def add_item(name: str, items: list[str] | None = None) -> list[str]:
    if items is None:
        items = [] # Create a NEW list only when needed
        items.append(name)
        return items
    