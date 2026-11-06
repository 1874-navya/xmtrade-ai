def discover_gold_symbol(symbols: list[str]) -> str | None:
    """Name-based candidate discovery; contract specifications still need manual verification."""
    exact = {s.upper(): s for s in symbols}
    for candidate in ("XAUUSD", "GOLD"):
        if candidate in exact:
            return exact[candidate]
    matches = [s for s in symbols if "XAUUSD" in s.upper()]
    return matches[0] if len(matches) == 1 else None
