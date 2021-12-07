def part1(input) -> int:
    return -1


if __name__ == "__main__":
    with open("sample.txt") as f:
        input = [l for l in f.readlines()]
        # input = [int(n) for n in f.read().split(",")]
    print(f"part 1: {part1(input)}")
