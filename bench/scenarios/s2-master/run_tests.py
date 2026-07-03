from tax import gross, TAX_RATE


def main():
    assert TAX_RATE == 0.20, "tax rate"
    assert gross(100) == 120.00, "gross of 100"
    print("ALL TESTS PASS")


if __name__ == "__main__":
    main()
