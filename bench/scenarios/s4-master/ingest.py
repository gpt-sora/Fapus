import os

from parser import parse_names


def load_names(path):
    with open(path, "rb") as f:
        return parse_names(f.read())
