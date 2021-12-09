from typing import Optional


class HeightMap:
    def __init__(self, map: list[list[int]]):
        self.map = map
        self.ylen = len(map)
        self.xlen = len(map[0])

    def get_lows(self) -> list[int]:
        lows = []
        for y in range(self.ylen):
            for x in range(self.xlen):
                val = self.get_at(x, y)
                adj = self._adj_values(x, y)
                if all([b > val for b in adj]):
                    lows.append(val)
        return lows

    def get_basins(self) -> list[list[int]]:
        basins = []

        def contains(x, y) -> bool:
            for basin in basins:
                for a, b in basin:
                    if x == a and y == b:
                        return True
            return False

        for y in range(self.ylen):
            for x in range(self.xlen):
                if contains(x, y):
                    continue
                if basin := self.basin(x, y):
                    basins.append(basin)
        return basins

    def basin(self, x: int, y: int, visited=None) -> Optional[list[int]]:
        if self.get_at(x, y) == 9:
            return None
        visited = []
        self._rec_basin(x, y, visited)
        return [c for c in set(visited)]  # unique

    def _rec_basin(self, x: int, y: int, visited):
        if self.get_at(x, y) == 9:
            return
        visited.append((x, y))
        for a, b in filter(lambda c: c not in visited, self._adj_coords(x, y)):
            self._rec_basin(a, b, visited)

    def get_at(self, x: int, y: int) -> int:
        return self.map[y][x]

    def _adj_values(self, x: int, y: int) -> list[int]:
        l = []
        if x < self.xlen - 1:
            l.append(self.map[y][x + 1])
        if x >= 1:
            l.append(self.map[y][x - 1])
        if y < self.ylen - 1:
            l.append(self.map[y + 1][x])
        if y >= 1:
            l.append(self.map[y - 1][x])
        return l

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
    with open("input.txt") as f:
        height_map = HeightMap(
            [[int(n) for n in line.strip()] for line in f.readlines()]
        )
    print(f"part 1: {part1(height_map)}")
    print(f"part 2: {part2(height_map)}")
