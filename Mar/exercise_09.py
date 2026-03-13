def get_age(
        registry: dict[str, int],
        name: str,
) -> int | None:
    return registry.get(name)