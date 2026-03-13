def track_savings(
        amount: float,
        savings: list[float] | None = None,
) -> list[float]:
    """ Tracks savings."""
    if savings is None:
        savings = []
        savings.append(amount)
    return savings