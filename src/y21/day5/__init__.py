from itertools import repeat
from typing import Counter
from functools import cached_property


class Segment:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @classmethod
    def from_str(cls, s: str):
        [a, b] = s.split(" -> ")
        [x1, y1] = a.split(",")
        [x2, y2] = b.split(",")
        return cls(int(x1), int(y1), int(x2), int(y2))

    def ortho(self) -> bool:
        return (self.x1 == self.x2) or (self.y1 == self.y2)

    @cached_property
    def coords(self) -> list[tuple[int, int]]:
        if self.x1 > self.x2:
            xs = range(self.x1, self.x2 - 1, -1)
        elif self.x1 == self.x2:
            xs = repeat(self.x1, abs(self.y1 + self.y2) + 1)
        else:
            xs = range(self.x1, self.x2 + 1)

        if self.y1 > self.y2:
            ys = range(self.y1, self.y2 - 1, -1)
        elif self.y1 == self.y2:
            ys = repeat(self.y1, abs(self.x1 + self.x2) + 1)
        else:
            ys = range(self.y1, self.y2 + 1)

        return [(a, b) for a, b in zip(xs, ys)]


def part1(segments: list[Segment]) -> int:
    coords = []
    for seg in segments:
        if seg.ortho():
            coords.extend(seg.coords)
    counts = Counter(coords)
    return sum([1 for c in counts.values() if c >= 2])


def part2(segments: list[Segment]) -> int:
    coords = []
    for seg in segments:
        coords.extend(seg.coords)
    counts = Counter(coords)
    return sum([1 for c in counts.values() if c >= 2])


if __name__ == "__main__":
    with open("y21/day5/input.txt") as f:
        segments = [Segment.from_str(l.strip()) for l in f.readlines()]
    print(f"part 1: {part1(segments)}")
    print(f"part 2: {part2(segments)}")
