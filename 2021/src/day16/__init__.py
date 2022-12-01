import abc
from functools import reduce
from itertools import chain

mapping = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


class Packet(abc.ABC):
    def __init__(
        self,
        version: int,
        type_id: int,
    ):
        self.version = version
        self.type_id = type_id

    @abc.abstractmethod
    def value(self) -> int:
        raise NotImplementedError


class Literal(Packet):
    def __init__(
        self,
        version: int,
        type_id: int,
        decimal: int,
    ):
        super().__init__(version, type_id)
        self.decimal = decimal

    def value(self) -> int:
        return self.decimal


class Operator(Packet):
    def __init__(self, version: int, type_id: int):
        super().__init__(version, type_id)
        self.subs = []

    def add(self, p: Packet):
        self.subs.append(p)

    def value(self) -> int:
        match self.type_id:
            case 0:
                return sum(s.value() for s in self.subs)
            case 1:
                if len(self.subs) == 1:
                    return self.subs[0].value()
                return reduce(lambda acc, x: acc * x, [s.value() for s in self.subs])
            case 2:
                return min([s.value() for s in self.subs])
            case 3:
                return max([s.value() for s in self.subs])
            case 5:
                v1 = self.subs[0].value()
                v2 = self.subs[1].value()
                return 1 if v1 > v2 else 0
            case 6:
                v1 = self.subs[0].value()
                v2 = self.subs[1].value()
                return 1 if v1 < v2 else 0
            case 7:
                v1 = self.subs[0].value()
                v2 = self.subs[1].value()
                return 1 if v1 == v2 else 0
            case n:
                raise Exception(f"invalid type id: {n}")


def substr(s: str, n: int) -> tuple[str, str]:
    return s[:n], s[n:]


def bin_to_int(b) -> int:
    return int(b, base=2)


class Transmission:
    def __init__(self, bits: str):
        self.bits = bits

    def decode(self) -> list[Packet]:
        packets = []
        self._decode(self.bits, packets)
        return packets

    def _decode(self, bits: str, packets: list):
        if bits == "" or "1" not in bits:
            return None, ""

        vs, tail = substr(bits, 3)
        ts, tail = substr(tail, 3)
        version = bin_to_int(vs)
        type_id = bin_to_int(ts)

        if type_id == 4:
            return self._literal(version, type_id, tail, packets)
        return self._operator(version, type_id, tail, packets)

    def _literal(
        self,
        version: int,
        type_id: int,
        bits: str,
        packets: list[Packet],
    ):
        ii = 0
        acc = []
        while True:
            g = bits[ii : ii + 5]
            acc.append(g[1:])
            ii += 5
            if g[0] == "0":
                break
        d = bin_to_int("".join(acc))
        p = Literal(version, type_id, d)
        packets.append(p)
        return p, bits[ii:]

    def _operator(
        self,
        version: int,
        type_id: int,
        bits: str,
        packets: list[Packet],
    ):
        pack = Operator(version, type_id)
        packets.append(pack)
        if bits[0] == "0":  # next 15 bits are sub-packets
            length = bin_to_int(bits[1:16])
            subs = bits[16 : 16 + length]
            while subs:
                p, subs = self._decode(subs, packets)
                pack.add(p)  # type: ignore
            tail = bits[16 + length :]
        else:  # next 11 bits are number of sub-packets
            n = bin_to_int(bits[1:12])
            tail = bits[12:]
            for _ in range(n):
                p, tail = self._decode(tail, packets)
                pack.add(p)  # type: ignore
        return pack, tail

    @classmethod
    def from_hex(cls, s: str):
        return cls("".join(chain([mapping[c] for c in s.strip()])))


def part1(hex: str) -> int:
    trans = Transmission.from_hex(hex)
    packets = trans.decode()
    return sum([p.version for p in packets])


def part2(hex: str) -> int:
    trans = Transmission.from_hex(hex)
    packets = trans.decode()
    return packets[0].value()


if __name__ == "__main__":
    with open("day16/input.txt") as f:
        line = f.read()
    print(f"part 1: {part1(line)}")
    print(f"part 2: {part2(line)}")
