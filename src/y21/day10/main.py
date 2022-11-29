from collections import deque
from functools import reduce
from typing import Counter


def matches(a: str, b: str) -> bool:
    return a + b in ["()", "[]", "{}", "<>"]


cmap = {")": "(", "]": "[", "}": "{", ">": "<"}
omap = {"(": ")", "[": "]", "{": "}", "<": ">"}


def is_corrupted(line: str) -> tuple[bool, str]:
    state = deque()
    for ch in line:
        if ch in cmap:
            if not matches(state[-1], ch):
                return True, ch
            state.pop()
        else:
            state.append(ch)
    return False, ""


def part1(input: list[str]) -> tuple[list[str], int]:
    incomplete = []
    corrupted = []
    for line in input:
        t, c = is_corrupted(line)
        if t:
            corrupted.append(c)
        else:
            incomplete.append(line)
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    return incomplete, sum(points[c] * n for c, n in Counter(corrupted).items())


def repair(line: str) -> str:
    state = deque()
    for ch in line:
        if ch in cmap:
            if matches(state[-1], ch):
                state.pop()
        else:
            state.append(ch)
    return "".join([omap[c] for c in reversed(state)])


def part2(input: list[str]) -> int:
    points = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = [
        reduce(lambda acc, c: acc * 5 + points[c], repair(line), 0) for line in input
    ]
    s = sorted(scores)
    return s[len(s) // 2]


if __name__ == "__main__":
    with open("input.txt") as f:
        input = [l.strip() for l in f.readlines()]
    in2, p1 = part1(input)
    print(f"part 1: {p1}")
    print(f"part 2: {part2(in2)}")
