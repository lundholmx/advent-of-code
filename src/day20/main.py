from typing import Literal

Boundary = Literal[".", "#"]


class Image:
    def __init__(self, image: list[list[str]]):
        self.image = image
        self.xlen = len(image[0])
        self.ylen = len(image)

    def pixel(self, x: int, y: int) -> list[str]:
        f = []
        for yy in range(y - 1, y + 2):
            for xx in range(x - 1, x + 2):
                f.append(self.get(xx, yy))
        return f

    def get(self, x, y) -> str:
        return self.image[y][x]

    def count(self) -> int:
        count = 0
        for row in self.image:
            for c in row:
                if c == "#":
                    count += 1
        return count


def expand(image: Image, boundary: Boundary, size: int = 2) -> Image:
    width = image.xlen + size * 2
    rows = []
    for _ in range(size):
        rows.append([boundary for _ in range(width)])

    for row in image.image:
        new = []
        for _ in range(size):
            new.append(boundary)
        for c in row:
            new.append(c)
        for _ in range(size):
            new.append(boundary)
        rows.append(new)

    for _ in range(size):
        rows.append([boundary for _ in range(width)])

    return Image(rows)


def transform(algorithm: str, image: Image, boundary: Boundary) -> Image:
    def mapping(n: list[str]) -> str:
        s = "".join(["0" if c == "." else "1" for c in n])
        index = int(s, base=2)
        return algorithm[index]

    image = expand(image, boundary)
    rows = []
    for y in range(1, image.ylen - 1):
        row = []
        for x in range(1, image.xlen - 1):
            f = image.pixel(x, y)
            s = mapping(f)
            row.append(s)
        rows.append(row)
    new = Image(rows)
    return new


def run(algo: str, image: Image, times: int) -> int:
    result: Image = image
    for ii in range(times):
        b = "." if ii % 2 == 0 else "#"
        result = transform(algo, result, b)
    return result.count()


def part1(algo: str, image: Image) -> int:
    return run(algo, image, 2)


def part2(algo: str, image: Image) -> int:
    return run(algo, image, 50)


def read_input(lines: list[str]) -> tuple[str, Image]:
    algorithm = lines[0]
    image = [[c for c in line] for line in lines[2:]]
    return algorithm, Image(image)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    algo, image = read_input(lines)
    print(f"part 1: {part1(algo, image)}")
    print(f"part 2: {part2(algo, image)}")
