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


class Name:
    def __init__(self, field):
        self.field = field

    @classmethod
    def cmethod(cls):
        return cls("field")


def convert(raw: Any):
    return f"raw:{raw}"


if __name__ == "__main__":
    items = Input("yYY/dayDD/input.txt", linetype="lines")\
        .add_map(convert)\
        .read()
    print("TODO")
