def part1(ins):
    h = 0
    v = 0
    for a, b in ins:
        match a:
            case "forward":
                h += b
            case "down":
                v += b
            case "up":
                v -= b
    return h * v


def part2(ins):
    h = 0
    v = 0
    aim = 0
    for a, b in ins:
        match a:
            case "forward":
                h += b
                v += aim * b
            case "down":
                aim += b
            case "up":
                aim -= b
    return h * v


if __name__ == "__main__":

    def parse(line: str):
        [a, b] = line.split(" ")
        return a, int(b)

    with open("day2/input.txt") as f:
        input = [parse(l) for l in f.readlines()]
    print(f"part 1: {part1(input)}")
    print(f"part 2: {part2(input)}")
