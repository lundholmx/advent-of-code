from dataclasses import dataclass

point = tuple[int, int, int]


def in_init_area(p: tuple[int, int]) -> bool:
    return p[0] >= -50 and p[1] <= 50


@dataclass
class Cuboid:
    xs: tuple[int, int]
    ys: tuple[int, int]
    zs: tuple[int, int]

    def get_coords(self) -> set[point]:
        x1, x2 = self.xs
        y1, y2 = self.ys
        z1, z2 = self.zs
        coords = set()
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    coords.add((x, y, z))
        return coords

    def init_area(self) -> bool:
        return all(in_init_area(p) for p in [self.xs, self.ys, self.zs])


@dataclass
class Step:
    on: bool
    cuboid: Cuboid


def part1(steps: list[Step]) -> int:
    coords = set()
    for s in filter(lambda s: s.cuboid.init_area(), steps):
        cs = s.cuboid.get_coords()
        if s.on:
            coords = coords.union(cs)
        else:
            coords = coords.difference(cs)
    return len(coords)


def read_input(lines: list[str]) -> list[Step]:
    def split_range(r):
        [_, ns] = r.split("=")
        [a, b] = ns.split("..")
        return int(a), int(b)

    steps = []
    for line in lines:
        [state, ranges] = line.split()
        on = True if state == "on" else False
        [xs, ys, zs] = ranges.split(",")
        c = Cuboid(split_range(xs), split_range(ys), split_range(zs))
        steps.append(Step(on, c))
    return steps


if __name__ == "__main__":
    with open("day22/input.txt") as f:
        input = [l.strip() for l in f.readlines()]
    steps = read_input(input)
    print(f"part 1: {part1(steps)}")
