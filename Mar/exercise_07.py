def calculate_travel_budget(
        base_cost: float, 
        flight_cost: float,
        buffer_percent: float = .1,
) -> float:
    # Adds base and flight costs, then multiplies by 1 + buffer 
    return (base_cost + flight_cost) * (1 + buffer_percent)