import os

from ingest import load_names


def main():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "names.txt")
    names = load_names(path)
    assert names == ["Ada", "Grace", "Édouard"], names
    print("ALL TESTS PASS")


if __name__ == "__main__":
    main()
