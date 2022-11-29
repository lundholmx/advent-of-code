from typing import Optional

point = tuple[int, int]


class Probe:
    def __init__(self, xtarget: point, ytarget: point):
        self.xpos = 0
        self.ypos = 0
        self.xtarget = xtarget
        self.ytarget = ytarget

    def find_steps(self) -> list[int]:
        results = []
        for vy in range(self.ytarget[0], 125):
            for vx in range(0, self.xtarget[1] + 1):
                if (res := self.calc(vx, vy)) is not None:
                    results.append(res)
        return results

    def calc(self, vx: int, vy: int) -> Optional[int]:
        curr_vx = vx
        curr_vy = vy
        ymax = 0
        xpos = 0
        ypos = 0
        while not self.beyond(xpos, ypos):
            xpos += curr_vx
            ypos += curr_vy
            if ypos > ymax:
                ymax = ypos

            if self.within(xpos, ypos):
                return ymax

            curr_vx = curr_vx - 1 if curr_vx > 0 else 0
            curr_vy -= 1

    def within(self, x: int, y: int) -> bool:
        x1, x2 = self.xtarget
        y1, y2 = self.ytarget
        return (x1 <= x <= x2) and (y1 <= y <= y2)

    def beyond(self, x: int, y: int) -> bool:
        return x > self.xtarget[1] or y < self.ytarget[0]


def parse(line: str) -> tuple[point, point]:
    def spl(aa: str) -> point:
        [_, rr] = aa.split("=")
        [a, b] = rr.split("..")
        return int(a), int(b)

    s = line.lstrip("target area: ")
    [xt, yt] = s.split(", ")
    return spl(xt), spl(yt)


def part1(probe: Probe) -> int:
    return max(probe.find_steps())


def part2(probe: Probe) -> int:
    return len(probe.find_steps())


if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.read().strip()
        xtarget, ytarget = parse(line)
    probe = Probe(xtarget, ytarget)
    print(f"part 1: {part1(probe)}")
    print(f"part 2: {part2(probe)}")
