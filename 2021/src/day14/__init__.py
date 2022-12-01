from collections import defaultdict
from itertools import pairwise


def parse_input(lines: list[str]) -> tuple[str, dict]:
    template = lines[0]
    rules = {}
    for line in lines[2:]:
        [a, b] = line.split(" -> ")
        rules[a] = b
    return template, rules


def calc(template: str, rules: dict[str, str], nsteps: int) -> int:
    formula = defaultdict(int)
    for a, b in pairwise(template):
        formula[a + b] += 1

    counter = defaultdict(int)
    for c in template:
        counter[c] += 1

    for _ in range(nsteps):
        next = defaultdict(int)
        for p, count in formula.items():
            r = rules[p]
            next[p[0] + r] += count
            next[r + p[1]] += count
            counter[r] += count
        formula = next
    values = counter.values()
    return max(values) - min(values)


if __name__ == "__main__":
    with open("day14/input.txt") as f:
        template, rules = parse_input([l.strip() for l in f.readlines()])
    print(f"part 1: {calc(template, rules, 10)}")
    print(f"part 2: {calc(template, rules, 40)}")
