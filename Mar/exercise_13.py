def finalize_relocation(
        destination: str,
        /, # Positional-only marker
        savings: list[float] | None = None,
        *, # Keyword-only marker
        currency: str = "USD"
) -> bool:
    """Finalizes the relocation plan."""
    if savings is None:
        savings = []
    return True