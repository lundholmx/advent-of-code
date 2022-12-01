from collections import defaultdict
from typing import Any, Callable


def part1(input: list[tuple[list, list]]) -> int:
    counts = defaultdict(int)
    for _, output in input:
        for o in output:
            counts[len(o)] += 1
    return sum(counts[p] for p in [2, 4, 3, 7])


def find(iter: list[Any], pred: Callable[[Any], bool]):
    for item in iter:
        if pred(item):
            return item
    raise Exception("not found")


def contains(a: str, b: str) -> bool:
    """Returns true if a contains all chars in b."""
    return all([c in a for c in b])


def containing(a: str, b: str) -> int:
    """Returns how many chars a contains of b."""
    return sum([1 for c in b if c in a])


def sort_str(s: str) -> str:
    return "".join(sorted(s))


def decode(signals: list[str], output: list[str]) -> int:
    one = find(signals, lambda s: len(s) == 2)
    four = find(signals, lambda s: len(s) == 4)
    seven = find(signals, lambda s: len(s) == 3)
    eight = find(signals, lambda s: len(s) == 7)
    ordered = {sort_str(s): n for s, n in zip([one, four, seven, eight], [1, 4, 7, 8])}
    unknown = filter(lambda s: s not in [one, four, seven, eight], signals)
    while len(ordered) < 10:
        found = {}
        for signal in unknown:
            if len(signal) == 5:  # 2, 3 or 5
                if all([contains(signal, one), contains(signal, seven)]):
                    found[signal] = 3
                elif containing(signal, four) == 3:
                    found[signal] = 5
                else:
                    found[signal] = 2
            elif len(signal) == 6:  # 0, 6 or 9
                if contains(signal, four):
                    found[signal] = 9
                elif contains(signal, one) and contains(signal, seven):
                    found[signal] = 0
                else:
                    found[signal] = 6
        unknown = filter(lambda s: s not in found, unknown)
        for sig, num in found.items():
            ordered[sort_str(sig)] = num

    nums = [ordered[sort_str(s)] for s in output]
    return int("".join([str(n) for n in nums]))


def part2(pairs) -> int:
    return sum([decode(signal, output) for signal, output in pairs])


if __name__ == "__main__":
    entries = []
    with open("day8/input.txt") as f:
        for line in f.readlines():
            [head, tail] = line.strip().split(" | ")
            entries.append((head.split(" "), tail.split(" ")))
    print(f"part 1: {part1(entries)}")
    print(f"part 2: {part2(entries)}")
