import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import cache, reduce
from typing import Any, Optional

import numpy as np

from lib import Input


@dataclass
class Datac:
    field: Any

    def method(self):
        pass


class Name:
    def __init__(self, field):
        self.field = field

    @classmethod
    def cmethod(cls):
        return cls("field")

    def method(self):
        pass


def convert(raw: Any):
    return f"raw:{raw}"


def part1(items):
    return len(items)


def part2(items):
    return len(items)


if __name__ == "__main__":
    items = Input("y22/day1/input.txt", linetype="lines").add_map(convert).read()
    print(part1(items), part2(items))
