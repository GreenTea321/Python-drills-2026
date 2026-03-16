def apply_discounts(prices: list[float], discount_rate: float) -> list[float]:
    # Subtracts the discount rate from 1 and multiplies
    return [price * (1 - discount_rate) for price in prices]