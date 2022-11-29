from abc import ABC, abstractmethod
from collections import Counter


class Node(ABC):
    def __init__(self, value: str):
        self.value = value
        self.small = value.lower() == value
        self.connected = []

    def connect(self, node):
        if not any(n.value == node.value for n in self.connected):
            self.connected.append(node)

    @abstractmethod
    def paths(self, acc: list, path: list[str]):
        raise NotImplementedError


class NodeV1(Node):
    def paths(self, acc: list, path: list[str]):
        if self.small and self.value in path:
            return
        this = list(e for e in path) + [self.value]
        acc.append(this)
        if self.value == "end":
            return
        for n in self.connected:
            n.paths(acc, this)


class NodeV2(Node):
    def paths(self, acc: list, path: list[str]):
        if self.value == "start" and self.value in path:
            return
        counts = Counter([p for p in path if p.lower() == p])
        this_count = counts.get(self.value, 0) == 1 and self.small
        if any([True for v in counts.values() if this_count and v == 2]):
            return
        occurrences = sum(1 for v in path if v == self.value)
        if self.small and occurrences == 2:
            return
        this = list(e for e in path) + [self.value]
        acc.append(this)
        if self.value == "end":
            return
        for n in self.connected:
            n.paths(acc, this)


def filter_valid(paths: list[list[str]]) -> list[list[str]]:
    return [p for p in paths if p[0] == "start" and p[-1] == "end"]


class Graph:
    def __init__(self, start: Node):
        self.start = start

    def paths(self):
        acc = []
        self.start.paths(acc, [])
        return filter_valid(acc)


def build(lines: list[str], cls) -> Graph:
    nodes = {}
    for line in lines:
        [a, b] = line.split("-")
        node_a = nodes.get(a, cls(a))
        if not a in nodes:
            nodes[a] = node_a
        node_b = nodes.get(b, cls(b))
        if not b in nodes:
            nodes[b] = node_b
        node_a.connect(node_b)
        node_b.connect(node_a)
    return Graph(nodes["start"])


def part1(graph: Graph) -> int:
    return len(graph.paths())


def part2(graph: Graph) -> int:
    return len(graph.paths())


if __name__ == "__main__":
    with open("y21/day12/input.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    print(f"part 1: {part1(build(lines, NodeV1))}")
    print(f"part 2: {part2(build(lines, NodeV2))}")
