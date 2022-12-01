from dataclasses import dataclass
from functools import cache


def next_pos(pos: int, steps: int) -> int:
    return (pos + steps - 1) % 10 + 1


@dataclass
class Dice:
    value: int = 0
    count: int = 0

    def roll(self) -> int:
        self.count += 1
        self.value = (self.value) % 100 + 1
        return self.value


def part1(p1: int, p2: int) -> int:
    dice = Dice()
    p1_score = 0
    p2_score = 0
    while True:
        d = sum(dice.roll() for _ in range(3))
        p1 = next_pos(p1, d)
        p1_score += p1
        if p1_score >= 1000:
            return p2_score * dice.count

        d = sum(dice.roll() for _ in range(3))
        p2 = next_pos(p2, d)
        p2_score += p2
        if p2_score >= 1000:
            return p1_score * dice.count


dice_sums = [a + b + c for a in range(1, 4) for b in range(1, 4) for c in range(1, 4)]


@cache
def dirac(
    turn: int,
    p1_pos: int,
    p1_score: int,
    p2_pos: int,
    p2_score: int,
):
    if p1_score >= 21:
        return 1, 0
    if p2_score >= 21:
        return 0, 1
    if turn % 2 == 0:
        ps = [next_pos(p1_pos, s) for s in dice_sums]
        results = [dirac(turn + 1, p, p1_score + p, p2_pos, p2_score) for p in ps]
    else:
        ps = [next_pos(p2_pos, s) for s in dice_sums]
        results = [dirac(turn + 1, p1_pos, p1_score, p, p2_score + p) for p in ps]
    return sum([n for n, _ in results]), sum([n for _, n in results])


def part2(p1: int, p2: int) -> int:
    c1, c2 = dirac(0, p1, 0, p2, 0)
    return max(c1, c2)


if __name__ == "__main__":
    with open("day21/input.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    p1, p2 = int(lines[0].split()[4]), int(lines[1].split()[4])
    print(f"part 1: {part1(p1, p2)}")
    print(f"part 2: {part2(p1, p2)}")
