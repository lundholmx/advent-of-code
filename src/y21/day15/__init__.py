import heapq
import sys
from collections import defaultdict

Point = tuple[int, int]
Map = list[list[int]]


class Dijkstra:
    def __init__(self, map: Map):
        self.map = map
        self.xlen = len(map[0])
        self.ylen = len(map)

    def neighbors(self, p: Point) -> list[Point]:
        x, y = p
        return [
            (a, b)
            for a, b in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            if 0 <= a < self.xlen and 0 <= b < self.ylen
        ]

    def shortest(self) -> int:
        target = (self.xlen - 1, self.ylen - 1)
        dist = {}
        queue = []
        for x in range(self.xlen):
            for y in range(self.ylen):
                p = (x, y)
                dist[p] = sys.maxsize
                if p != (0, 0):
                    heapq.heappush(queue, (sys.maxsize, p))
        dist[(0, 0)] = 0
        heapq.heappush(queue, (1, (0, 0)))

        visited = set()
        while queue:
            _, u = heapq.heappop(queue)
            if u in visited:
                continue

            ns = [n for n in self.neighbors(u) if n not in visited]
            for v in ns:
                alt = dist[u] + self._value(v)
                if alt < dist[v]:
                    dist[v] = alt
                    heapq.heappush(queue, (alt, v))
            if u == target:
                return dist[target]
            visited.add(u)
        raise Exception("failed to reach target node")

    def _value(self, p: Point) -> int:
        x, y = p
        return self.map[y][x]


def part1(map: Map) -> int:
    return Dijkstra(map).shortest()


def add(a, n):
    if a + n < 10:
        return a + n
    return a + n - 9


def part2(map: Map) -> int:
    def inc(m, a):
        return [[add(n, a) for n in row] for row in m]

    r1 = [inc(map, n) for n in range(5)]
    r2 = [inc(r1[1], n) for n in range(5)]
    r3 = [inc(r2[1], n) for n in range(5)]
    r4 = [inc(r3[1], n) for n in range(5)]
    r5 = [inc(r4[1], n) for n in range(5)]

    new_map = []
    for rowmatrix in [r1, r2, r3, r4, r5]:
        lines = defaultdict(list)
        index = 0
        for m in rowmatrix:
            for i, line in enumerate(m):
                index = i
                lines[i].extend(line)
        for ii in range(index + 1):
            new_map.append(lines[ii])
    return Dijkstra(new_map).shortest()


if __name__ == "__main__":
    with open("y21/day15/input.txt") as f:
        map = [[int(n) for n in l.strip()] for l in f.readlines()]
    print(f"part 1: {part1(map)}")
    print(f"part 2: {part2(map)}")
