from typing import Optional, Union
import math
import itertools


class Node:
    def __init__(self, parent: "Node", value: int=None):
        self.parent = parent
        self.value: Optional[int] = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None

    @classmethod
    def new_root(cls, left, right):
        c = cls(None)
        c.left = left
        c.right = right
        return c

    def magnitude(self) -> int:
        if self.value is not None:
            return self.value
        return 3*self.left.magnitude() + 2 * self.right.magnitude()

    def to_list(self) -> Union[list, int]:
        if self.value is not None:
            return self.value
        return [self.left.to_list(), self.right.to_list()]

    def __str__(self) -> str:
        if self.value is not None:
            return f"{self.value}"
        return f"node({self.left}, {self.right})"
    
    # def reduce(self, level: int) -> Optional["Node"]:
    #     if self.value is None and level == 4: # explode!
    #         if (right := self.parent.right_up(self)):
    #             right.value += self.right.value
    #         if left := self.parent.left_up(self):
    #             left.value += self.left.value
    #         self.value = 0
    #         self.left = None
    #         self.right = None
    #         return self

    #     if self.value is not None and self.value >= 10:
    #         self.left = Node(self, math.floor(self.value / 2))
    #         self.right = Node(self, math.ceil(self.value / 2))
    #         self.value = None
    #         if level == 4:
    #             return self.reduce(level)
    #         return self

    #     n = None
    #     if self.left:
    #         n = self.left.reduce(level+1)
    #     if self.right and not n:
    #         n  = self.right.reduce(level+1)
    #     return n
    
    def explode(self, level: int) -> Optional["Node"]:
        if self.value is None and level == 4: # explode!
            if (right := self.parent.right_up(self)):
                right.value += self.right.value
            if left := self.parent.left_up(self):
                left.value += self.left.value
            self.value = 0
            self.left = None
            self.right = None
            return self

        n = None
        if self.left:
            n = self.left.explode(level+1)
        if self.right and not n:
            n  = self.right.explode(level+1)
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
            n = self.left.split(level+1)
        if self.right and not n:
            n  = self.right.split(level+1)
        return n

    def right_up(self, src):
        if self.value is not None:
            return self

        if self.parent is None: # root
            if self.left is src and self.right:
                return self.right.left_down()
            else:
                return None

        if src is self.right:
            return self.parent.right_up(self)
        elif src is self.left and self.right:
            return self.right.left_down()

    def left_up(self, src):
        if self.value is not None:
            return self

        if self.parent is None: # root
            if self.right is src and self.left:
                return self.left.right_down()
            else:
                return None

        if src is self.left:
            return self.parent.left_up(self)
        elif src is self.right and self.left:
            return self.left.right_down()

    def left_down(self):
        if self.value is not None:
            return self
        if self.left:
            return self.left.left_down()

    def right_down(self):
        if self.value is not None:
            return self
        if self.right:
            return self.right.right_down()



class Number:
    def __init__(self, root: Node):
        self.root = root

    def reduce(self):
        n = self.root.explode(0)
        if not n:
            n = self.root.split(0)
        return n

    def __str__(self) -> str:
        return self.root.__str__()

    def to_list(self):
        return self.root.to_list()

    def reduce_all(self):
        while self.reduce():
            pass

    def magnitude(self) -> int:
        return self.root.magnitude()

# TODO: use singledispath


def build_node(parent: Node, value) -> Node:
    if isinstance(value, int):
        return Node(parent, value)
    node = Node(parent)
    node.left =  build_node(node, value[0])
    node.right = build_node(node, value[1])
    return node


def build_tree(line: list) -> Number:
    root = Node(None) # type: ignore
    root.left = build_node(root, line[0])
    root.right = build_node(root, line[1])
    return Number(root)


def part1(lines: list) -> int:
    trees = [l for l in lines]
    result = build_tree(trees.pop(0))
    curr = result
    for ii, ls in enumerate(trees):
        tree = build_tree(ls)
        node = Node(None) # type: ignore
        node.left = build_node(node, curr.to_list())
        node.right = build_node(node, tree.to_list())
        number = Number(node)
        number.reduce_all()
        curr = number

    return curr.magnitude()


def part2(lines: list) -> int:
    largest = 0
    combos = itertools.combinations([l for l in lines], 2)
    for a, b in combos:
        # a + b
        number = build_tree([a, b])
        number.reduce_all()
        m = number.magnitude()
        if m > largest:
            largest= m
        # b + a
        number = build_tree([b, a])
        number.reduce_all()
        m = number.magnitude()
        if m > largest:
            largest= m
    return largest


if __name__ == "__main__":
    with open("input.txt") as f:
        input = [eval(l.strip()) for l in f.readlines()]
        # input = [int(n) for n in f.read().split(",")]
    # print(f"part 1: {part1(input)}")
    print(f"part 2: {part2(input)}")
