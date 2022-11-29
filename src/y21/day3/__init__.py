def count(ins: list[str], col: int) -> tuple[int, int]:
    ones = len([1 for row in range(len(ins)) if ins[row][col] == "1"])
    return ones, len(ins) - ones


def filter_col_type(rep: list[str], col: int, x: str):
    return list(filter(lambda n: n[col] == x, rep))


def rating(ins: list[str], msb: str, lsb: str, col: int = 0):
    if len(ins) == 1:
        return int(ins[0], 2)
    ones, zeros = count(ins, col)
    if (ones > zeros) or (ones == zeros):
        return rating(filter_col_type(ins, col, msb), msb, lsb, col + 1)
    else:
        return rating(filter_col_type(ins, col, lsb), msb, lsb, col + 1)


def part1(ins: list[str]):
    g = ""
    e = ""
    for col in range(len(ins[0]) - 1):
        ones, zeros = count(ins, col)
        if ones > zeros:
            g += "1"
            e += "0"
        else:
            g += "0"
            e += "1"
    return int(g, 2) * int(e, 2)


def part2(ins: list[str]):
    return rating(ins, "1", "0") * rating(ins, "0", "1")


if __name__ == "__main__":
    with open("y21/day3/input.txt") as f:
        input = [n for n in f.readlines()]
    print(f"part 1: {part1(input)}")
    print(f"part 2: {part2(input)}")
