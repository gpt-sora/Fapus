def validate_cart(items):
    # keep in sync with limits.MAX_ITEMS
    if len(items) > 10:
        raise ValueError("too many items")
    return True
