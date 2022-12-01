import itertools as it
from collections import defaultdict
from dataclasses import dataclass
from typing import Optional

Coord = tuple[int, int, int]


rotation_funcs = [
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (x, -y, z),
    lambda x, y, z: (x, y, -z),
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (x, z, y),
    lambda x, y, z: (x, -z, y),
    lambda x, y, z: (x, z, -y),
    lambda x, y, z: (x, -z, -y),
    lambda x, y, z: (-x, y, z),
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (-x, -y, -z),
    lambda x, y, z: (-x, z, y),
    lambda x, y, z: (-x, -z, y),
    lambda x, y, z: (-x, z, -y),
    lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: (y, x, z),
    lambda x, y, z: (y, -x, z),
    lambda x, y, z: (y, x, -z),
    lambda x, y, z: (y, -x, -z),
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (y, -z, x),
    lambda x, y, z: (y, z, -x),
    lambda x, y, z: (y, -z, -x),
    lambda x, y, z: (-y, x, z),
    lambda x, y, z: (-y, -x, z),
    lambda x, y, z: (-y, x, -z),
    lambda x, y, z: (-y, -x, -z),
    lambda x, y, z: (-y, z, x),
    lambda x, y, z: (-y, -z, x),
    lambda x, y, z: (-y, z, -x),
    lambda x, y, z: (-y, -z, -x),
    lambda x, y, z: (z, x, y),
    lambda x, y, z: (z, -x, y),
    lambda x, y, z: (z, x, -y),
    lambda x, y, z: (z, -x, -y),
    lambda x, y, z: (z, y, x),
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (z, y, -x),
    lambda x, y, z: (z, -y, -x),
    lambda x, y, z: (-z, x, y),
    lambda x, y, z: (-z, -x, y),
    lambda x, y, z: (-z, x, -y),
    lambda x, y, z: (-z, -x, -y),
    lambda x, y, z: (-z, y, x),
    lambda x, y, z: (-z, -y, x),
    lambda x, y, z: (-z, y, -x),
    lambda x, y, z: (-z, -y, -x),
]


def rotations(coord: Coord):
    x, y, z = coord
    return [f(x, y, z) for f in rotation_funcs]


@dataclass
class Scanner:
    reports: list[Coord]


def rotate(sc, f):
    return [f(a, b, c) for a, b, c in sc]


def check(sc_a: Scanner, sc_b: Scanner) -> Optional[tuple[Scanner, Coord]]:
    results = defaultdict(int)
    for x, y, z in sc_a.reports:
        for xp, yp, zp in sc_b.reports:
            for f in rotation_funcs:
                a, b, c = f(xp, yp, zp)
                r1 = x + a
                r2 = y + b
                r3 = z + c
                co = (r1, r2, r3)
                results[co] += 1
                if results[co] == 12:
                    rs = [(r1 - a, r2 - b, r3 - c) for a, b, c in rotate(sc_b.reports, f)]
                    return Scanner(rs), co


def part1(scanners: list[Scanner]) -> tuple[int, list[Coord]]:
    finished = [scanners[0]]
    left = scanners[1:]

    ps = []
    while left:
        add = []
        for scanner in finished:
            done = -1
            for ii in range(len(left)):
                res = check(scanner, left[ii])
                if res:
                    add.append(res[0])
                    ps.append(res[1])
                    done = ii
                    break

            if done >= 0:
                left.pop(done)
        for a in add:
            finished.append(a)

    coords = set()
    for sc in finished:
        for c in sc.reports:
            coords.add(c)

    return len(coords), ps


def manhattan(p1: Coord, p2: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(p1, p2))


def part2(ps: list[Coord]) -> int:
    return max([manhattan(p1, p2) for p1, p2 in it.combinations(ps, 2)])


def read_input(lines: list[str]) -> list[Scanner]:
    acc = []
    scanners = []

    for line in lines:
        if line == "":
            scanners.append(Scanner(acc))
            acc = []
        elif "scanner" in line:
            pass
        else:
            [a, b, c] = line.split(",")
            acc.append((int(a), int(b), int(c)))
    scanners.append(Scanner(acc))
    return scanners


if __name__ == "__main__":
    with open("day19/input.txt") as f:
        scanners = read_input([l.strip() for l in f.readlines()])
    p1, positions = part1(scanners)
    print(f"part 1: {p1}")
    print(f"part 2: {part2(positions)}")
