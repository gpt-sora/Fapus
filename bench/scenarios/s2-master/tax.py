TAX_RATE = 0.20


def gross(net):
    return round(net * (1 + TAX_RATE), 2)
