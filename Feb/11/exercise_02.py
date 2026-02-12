def check_price(shop_inventory: dict, item_name: str) -> str:
    #1. Get the price without an expelicit default.
    price = shop_inventory.get(item_name):

    #2. Logic check for None.
    if price is None:
        return "Item not found in stock."

    #3. Get a value with a forced default.
    tax_rate = shop_inventory.get("tax_rate", 0.08)

    total = price + (price * tax_rate)
    return f"The total cost for {item_name} is {total}"