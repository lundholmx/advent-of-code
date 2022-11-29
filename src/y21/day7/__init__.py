import statistics
import math


def part1(input: list[int]) -> int:
    weight = int(statistics.median(input))
    return sum([abs(n - weight) for n in input])


def part2(input: list[int]) -> int:
    mean = math.floor(statistics.mean(input))
    return sum([sum(range(abs(n - mean) + 1)) for n in input])


if __name__ == "__main__":
    with open("y21/day7/input.txt") as f:
        input = [int(n) for n in f.read().split(",")]
    print(f"part 1: {part1(input)}")
    print(f"part 2: {part2(input)}")
