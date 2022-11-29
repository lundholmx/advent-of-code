from typing import Optional


class HeightMap:
    def __init__(self, map: list[list[int]]):
        self.map = map
        self.ylen = len(map)
        self.xlen = len(map[0])

    def _iter(self):
        for y in range(self.ylen):
            for x in range(self.xlen):
                yield (x, y)

    def get_lows(self) -> list[int]:
        lows = []
        for x, y in self._iter():
            val = self.get_at(x, y)
            adj = self._adj_values(x, y)
            if all([b > val for b in adj]):
                lows.append(val)
        return lows

    def get_basins(self) -> list[list[int]]:
        basins = []
        visited = set()
        for x, y in self._iter():
            if (x, y) in visited:
                continue
            if basin := self.basin(x, y):
                basins.append(basin)
                for c in basin:
                    visited.add(c)
        return basins

    def basin(self, x: int, y: int) -> Optional[list[int]]:
        if self.get_at(x, y) == 9:
            return None
        visited = set()
        self._rec_basin(x, y, visited)
        return list(visited)

    def _rec_basin(self, x: int, y: int, visited: set):
        if self.get_at(x, y) == 9:
            return
        visited.add((x, y))
        for a, b in filter(lambda c: c not in visited, self._adj_coords(x, y)):
            self._rec_basin(a, b, visited)

    def get_at(self, x: int, y: int) -> int:
        return self.map[y][x]

    def _adj_values(self, x: int, y: int) -> list[int]:
        return [self.get_at(a, b) for a, b in self._adj_coords(x, y)]

    def _adj_coords(self, x: int, y: int) -> list[tuple[int, int]]:
        l = []
        if x < self.xlen - 1:
            l.append((x + 1, y))
        if x >= 1:
            l.append((x - 1, y))
        if y < self.ylen - 1:
            l.append((x, y + 1))
        if y >= 1:
            l.append((x, y - 1))
        return l


def part1(map: HeightMap) -> int:
    return sum([n + 1 for n in map.get_lows()])


def part2(map: HeightMap) -> int:
    sizes = sorted([len(b) for b in map.get_basins()])
    return sizes[-3] * sizes[-2] * sizes[-1]


if __name__ == "__main__":
    with open("y21/day9/input.txt") as f:
        map = HeightMap([[int(n) for n in line.strip()] for line in f.readlines()])
    print(f"part 1: {part1(map)}")
    print(f"part 2: {part2(map)}")
