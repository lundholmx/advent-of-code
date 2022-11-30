import numpy as np


def parse_input(lines: list[str]) -> tuple[np.ndarray, list[tuple[str, int]]]:
    coords = []
    sep_line = 0
    for ii, line in enumerate(lines):
        if line == "":
            sep_line = ii + 1
            break
        [col, row] = line.split(",")
        coords.append((int(row), int(col)))

    folds = []
    for line in lines[sep_line:]:
        [axis, n] = line.lstrip("fold along ").split("=")
        folds.append((axis, int(n)))

    nr = max([a for a, _ in coords]) + 1
    nc = max([a for _, a in coords]) + 1
    map = np.zeros((nr, nc), dtype=int)
    for row, col in coords:
        map[row, col] = 1
    return map, folds


def fold(map: np.ndarray, folds: list[tuple[str, int]]) -> np.ndarray:
    result = np.copy(map)
    for axis, value in folds:
        if axis == "y":
            top = result[:value, ...]
            bot = np.flipud(result[value + 1 :, ...])
            if bot.shape[0] < top.shape[0]:  # Check if we need padding
                row_diff = top.shape[0] - bot.shape[0]
                bot = np.vstack([np.zeros((row_diff, bot.shape[1])), bot])
            result = top + bot
        else:
            left = result[..., :value]
            right = np.fliplr(result[..., value + 1 :])
            result = left + right
    return result


def part1(map: np.ndarray, folds: list[tuple[str, int]]) -> int:
    result = fold(map, folds[:1])
    return np.count_nonzero(result)


def part2(map: np.ndarray, folds: list[tuple[str, int]]):
    result = fold(map, folds)
    for row in result:
        for col in row:
            s = "o" if col > 0 else " "
            print(s.ljust(2), end="")
        print()


if __name__ == "__main__":
    with open("y21/day13/input.txt") as f:
        map, folds = parse_input([l.strip() for l in f.readlines()])
    print(f"part 1: {part1(map, folds)}")
    print("part 2:")
    part2(map, folds)  # Should read eight capital letters
