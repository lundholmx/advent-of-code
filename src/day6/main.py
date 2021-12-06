from collections import Counter


def solve(input: list[int], ndays: int = 80) -> int:
    counts = {a:b for a, b in Counter(input).items()}
    for _ in range(ndays):
        n_resets = counts.get(0, 0)
        nc = {
            internal-1: count
            for internal, count in counts.items()
            if internal > 0
        }
        nc[8] = n_resets
        nc[6] = nc.get(6, 0) + n_resets
        counts = nc
    return sum([v for v in counts.values()])


if __name__ == "__main__":
    with open("input.txt") as f:
        input = [int(n) for n in f.read().strip().split(",")]
    print(f"part 1: {solve(input, 80)}")
    print(f"part 2: {solve(input, 256)}")
