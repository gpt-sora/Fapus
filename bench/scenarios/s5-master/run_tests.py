from stats import mean, median


def main():
    assert mean([1, 2, 3]) == 2, "mean"
    assert median([1, 3, 2]) == 2, "median odd"
    assert median([1, 2, 3, 4]) == 2.5, "median even"
    print("ALL TESTS PASS")


if __name__ == "__main__":
    main()
