import fileinput
import queue
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


Map = list[list[str]]

heights = {l: n + 1 for n, l in enumerate("abcdefghijklmnopqrstuvwxyz")}
heights["S"] = heights["a"]
heights["E"] = heights["z"]


class Node:
    def __init__(self, p: Point, parent):
        self.p = p
        self.parent = parent

    def __str__(self):
        return f"{self.p}"


def backtrack(n: Node, count: int = 0) -> int:
    return 1 + backtrack(n.parent) if n.parent else count


class BFS:
    def __init__(self, map: Map):
        self.map = map
        self.xlen = len(map[0])
        self.ylen = len(map)

    def find_all(self, letter: str):
        for x in range(self.xlen):
            for y in range(self.ylen):
                if self.map[y][x] == letter:
                    yield Point(x, y)

    def find(self, letter: str) -> Point:
        return next(self.find_all(letter))

    def shortest(self, start: Point, target: Point) -> int:
        root = Node(start, None)
        q = queue.Queue()
        q.put(root)

        visited = set()
        visited.add(start)

        while not q.empty():
            v = q.get()
            if v.p == target:
                return backtrack(v)
            for w in self._neighbors(v.p):
                if w not in visited:
                    visited.add(w)
                    q.put(Node(w, v))
        return self.xlen * self.ylen

    def _height(self, p: Point) -> int:
        return heights[self.map[p.y][p.x]]

    def _neighbors(self, p: Point) -> list[Point]:
        x, y = p
        return [
            Point(a, b)
            for a, b in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            if self._can_move_to(p, Point(a, b))
        ]

    def _can_move_to(self, a: Point, b: Point) -> bool:
        if not (0 <= b.x < self.xlen and 0 <= b.y < self.ylen):
            return False
        d = self._height(b) - self._height(a)
        return d <= 1


def part1(bfs: BFS) -> int:
    start = bfs.find("S")
    end = bfs.find("E")
    return bfs.shortest(start, end)


def part2(bfs: BFS) -> int:
    end = bfs.find("E")
    return min([bfs.shortest(start, end) for start in bfs.find_all("a")])


if __name__ == "__main__":
    map = [[c for c in line.strip()] for line in fileinput.input()]
    bfs = BFS(map)
    print(f"part 1: {part1(bfs)}")
    print(f"part 2: {part2(bfs)}")
