class Todo:
    def __init__(self):
        pass

    def meth(self) -> None:
        pass

    @classmethod
    def classmeth(cls):
        pass


def func(input) -> None:
    pass


def part1(input) -> int:
    return -1


if __name__ == "__main__":
    with open("sample.txt") as f:
        input = [l for l in f.readlines()]
        # input = [int(n) for n in f.read().split(",")]
    print(f"part 1: {part1(input)}")
