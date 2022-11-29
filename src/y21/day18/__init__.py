import itertools
import math
from typing import Optional, Union


class Node:
    def __init__(self, parent=None, value: int = None):
        self.parent = parent
        self.value: Optional[int] = value
        self.left = None
        self.right = None

    def magnitude(self) -> int:
        if self.value is not None:
            return self.value
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()  # type: ignore

    def to_list(self) -> Union[list, int]:
        if self.value is not None:
            return self.value
        return [self.left.to_list(), self.right.to_list()]  # type: ignore

    def explode(self, level: int) -> Optional["Node"]:
        if self.value is None and level == 4:
            if right := self.parent.right_up(self):  # type: ignore
                right.value += self.right.value  # type: ignore
            if left := self.parent.left_up(self):  # type: ignore
                left.value += self.left.value  # type: ignore
            self.value = 0
            self.left = None
            self.right = None
            return self

        n = None
        if self.left:
            n = self.left.explode(level + 1)
        if self.right and not n:
            n = self.right.explode(level + 1)
        return n

    def split(self, level: int) -> Optional["Node"]:
        if self.value is not None and self.value >= 10:
            self.left = Node(self, math.floor(self.value / 2))
            self.right = Node(self, math.ceil(self.value / 2))
            self.value = None
            if level == 4:
                return self.explode(level)
            return self

        n = None
        if self.left:
            n = self.left.split(level + 1)
        if self.right and not n:
            n = self.right.split(level + 1)
        return n

    def right_up(self, src):
        if self.value is not None:
            return self
        elif self.parent is None:
            if self.left is src and self.right:
                return self.right.left_down()
            else:
                return None
        elif src is self.right:
            return self.parent.right_up(self)
        elif src is self.left and self.right:
            return self.right.left_down()

    def left_up(self, src):
        if self.value is not None:
            return self
        elif self.parent is None:  # root
            if self.right is src and self.left:
                return self.left.right_down()
            else:
                return None
        elif src is self.left:
            return self.parent.left_up(self)
        elif src is self.right and self.left:
            return self.left.right_down()

    def left_down(self):
        if self.value is not None:
            return self
        elif self.left:
            return self.left.left_down()

    def right_down(self):
        if self.value is not None:
            return self
        elif self.right:
            return self.right.right_down()


class Number:
    def __init__(self, root: Node):
        self.root = root

    def reduce(self):
        n = self.root.explode(0)
        if not n:
            n = self.root.split(0)
        return n

    def to_list(self):
        return self.root.to_list()

    def reduce_all(self):
        while self.reduce():
            pass

    def magnitude(self) -> int:
        return self.root.magnitude()


def build_node(parent: Node, value) -> Node:
    if isinstance(value, int):
        return Node(parent, value)
    node = Node(parent)
    node.left = build_node(node, value[0])
    node.right = build_node(node, value[1])
    return node


def build_tree(line: list) -> Number:
    root = Node(None)  # type: ignore
    root.left = build_node(root, line[0])
    root.right = build_node(root, line[1])
    return Number(root)


def part1(lines: list) -> int:
    trees = [l for l in lines]
    result = build_tree(trees.pop(0))
    curr = result
    for ls in trees:
        number = build_tree([curr.to_list(), ls])
        number.reduce_all()
        curr = number
    return curr.magnitude()


def part2(lines: list) -> int:
    magnitudes = []
    for a, b in itertools.combinations(lines, 2):
        # a + b
        number = build_tree([a, b])
        number.reduce_all()
        magnitudes.append(number.magnitude())
        # b + a
        number = build_tree([b, a])
        number.reduce_all()
        magnitudes.append(number.magnitude())
    return max(magnitudes)


if __name__ == "__main__":
    with open("y21/day18/input.txt") as f:
        input = [eval(l.strip()) for l in f.readlines()]
    print(f"part 1: {part1(input)}")
    print(f"part 2: {part2(input)}")
