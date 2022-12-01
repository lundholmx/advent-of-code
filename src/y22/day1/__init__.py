from lib import Input


def group(items: list[str]) -> list[int]:
    found = []
    curr = 0
    for n in items:
        if n.strip() != "":
            curr += int(n)
        else:
            found.append(curr)
            curr = 0
    found.append(curr)
    return sorted(found, reverse=True)


if __name__ == "__main__":
    items = Input("y22/day1/input.txt", linetype="lines").read()
    items = group(items)
    print(f"Part 1: {items[0]}", f"Part 2: {sum(items[:3])}")
