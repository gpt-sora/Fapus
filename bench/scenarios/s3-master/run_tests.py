from cart import can_add


def main():
    assert can_add(list(range(24))) is True, "24 items: below cap"
    assert can_add(list(range(25))) is False, "25 items: at cap"
    print("ALL TESTS PASS")


if __name__ == "__main__":
    main()
