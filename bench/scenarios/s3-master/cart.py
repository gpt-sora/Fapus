from limits import MAX_ITEMS


def can_add(cart):
    return len(cart) < MAX_ITEMS
