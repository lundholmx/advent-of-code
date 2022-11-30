class Cavern:
    def __init__(self, map: list[list[int]]):
        self.map = map
        self.xlen = len(map[0])
        self.ylen = len(map)

    @classmethod
    def from_str(cls, s: str):
        return cls([[int(n) for n in line.strip()] for line in s.splitlines()])

    def step(self):
        ripples = set()
        for x in range(self.xlen):
            for y in range(self.ylen):
                v = self._inc(x, y)
                if v == 10 and (x, y) not in ripples:
                    self._ripple(x, y, ripples)
        flashes = 0
        for x in range(self.xlen):
            for y in range(self.ylen):
                if self[x, y] == 10:
                    self[x, y] = 0
                    flashes += 1
                else:
                    adj = self._adj(x, y)
                    if len(adj) == 8 and all([self[a, b] == 10 for a, b in adj]):
                        self[x, y] = 0
                        flashes += 1
        return flashes

    def _ripple(self, x: int, y: int, rs: set):
        if (x, y) in rs:
            return
        rs.add((x, y))
        adj = [(xx, yy) for xx, yy in self._adj(x, y) if self[xx, yy] < 10]
        for a, b in adj:
            if self._inc(a, b) == 10:
                self._ripple(a, b, rs)

    def _adj(self, c: int, r: int):
        coords = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
        return [(x + c, y + r) for x, y in coords if self._within(x + c, y + r) and (x, y) != (0, 0)]

    def _within(self, x: int, y: int) -> bool:
        return x >= 0 and x < self.xlen and y >= 0 and y < self.ylen

    def _inc(self, x: int, y: int) -> int:
        if (v := self[x, y]) < 10:
            self[x, y] = v + 1
            return v + 1
        else:
            return 10

    def __setitem__(self, key: tuple[int, int], value: int):
        x, y = key
        self.map[y][x] = value

    def __getitem__(self, key: tuple[int, int]) -> int:
        x, y = key
        return self.map[y][x]


def part1(cavern: Cavern) -> int:
    return sum(cavern.step() for _ in range(100))


def part2(cavern: Cavern) -> int:
    step = 100  # from part 1
    while True:
        if cavern.step() == 100:
            break
        step += 1
    return step + 1


if __name__ == "__main__":
    with open("y21/day11/input.txt") as f:
        map = Cavern.from_str(f.read())
    print(f"part 1: {part1(map)}")
    print(f"part 2: {part2(map)}")
