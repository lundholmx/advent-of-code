indexes = [(row, col) for row in range(5) for col in range(5)]


class Board:
    def __init__(self, board: list[list[tuple[int, bool]]]) -> None:
        self.board = board
        self.done = False

    def set(self, n: int):
        if self.done:
            return True

        for row, col in indexes:
            value, _ = self.board[row][col]
            if value == n:
                self.board[row][col] = (value, True)

        self.done = self.check()
        return self.done

    def check(self):
        if any([all([s for _, s in row]) for row in self.board]):
            return True
        return any(
            [all([self.board[row][col][1] for row in range(5)]) for col in range(5)]
        )

    def score(self, num: int):
        return num * sum([sum([n for n, m in row if not m]) for row in self.board])

    @classmethod
    def from_str_list(cls, lst):
        return cls([[(int(n), False) for n in line.split() if n != ""] for line in lst])


def parse_input(input: list[str]) -> tuple[list[int], list[Board]]:
    draws = input[0]

    acc = []
    boards = []
    for line in input[2:]:
        if line == "":
            boards.append(acc.copy())
            acc = []
        else:
            acc.append(line)
    boards.append(acc.copy())

    draw = [int(n) for n in draws.split(",")]
    games = [Board.from_str_list(b) for b in boards]
    return draw, games


def part1(draws: list[int], games: list[Board]):
    for n in draws:
        for g in games:
            if g.set(n):
                return g.score(n)


def part2(draws: list[int], games: list[Board]):
    wins = []
    for n in draws:
        for g in filter(lambda g: not g.done, games):
            if g.set(n):
                wins.append((n, g))
        if all([g.done for g in games]):
            break
    n, g = wins.pop()
    return g.score(n)


if __name__ == "__main__":
    with open("input.txt") as f:
        input = [l.strip() for l in f.readlines()]
    draws, boards = parse_input(input)
    print(f"part 1: {part1(draws, boards)}")
    draws, boards = parse_input(input)
    print(f"part 2: {part2(draws, boards)}")
