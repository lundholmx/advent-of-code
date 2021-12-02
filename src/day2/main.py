def part1(ins: list[str]):
    h = 0
    v = 0
    for ii in ins:
        [a, b] = ii.split(" ")
        match a:
            case "forward":
                h += int(b)
            case "down":
                v += int(b)
            case "up":
                v -= int(b)
    return h * v


def part2(ins: list[str]):
    h = 0
    v = 0
    aim = 0
    for ii in ins:
        [a, b] = ii.split(" ")
        match a:
            case "forward":
                h += int(b)
                v +=  aim * int(b)
            case "down":
                aim += int(b)
            case "up":
                aim -= int(b)
    return h * v


if __name__ == "__main__":
    with open("input.txt") as f:
        input = [n for n in f.readlines()]
    print(f"part 1: {part1(input)}")
    print(f"part 2: {part2(input)}")
