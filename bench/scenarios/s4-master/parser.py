def parse_names(text):
    """Split a comma-separated string of names, trimming whitespace."""
    return [p.strip() for p in text.split(",") if p.strip()]
