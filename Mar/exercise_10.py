def record_match(
        match_id: str,
        history: list[str] | None = None,        
) -> list[str]:
    if history is None:
        history = [] 
        history.append(match_id) 
    return history