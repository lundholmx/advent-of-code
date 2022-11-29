from typing import Any, Callable, Literal

LineType = Literal["multi", "single"]
MapFunc = Callable[[Any], Any]


class Input:
    def __init__(
        self,
        filepath: str,
        *,
        linetype: LineType = "multi",
        split_token: str = ",",
    ):
        self.filepath = filepath
        self._type = linetype
        self.split_token = split_token
        self._pipeline: list[MapFunc] = []

    def read(self) -> [Any]:
        with open(self.filepath) as f:
            lines = f.readlines()

        if self._type == "single":
            lines = lines[0].split(self.split_token)

        items = [self._map(item.rstrip()) for item in lines]
        return items

    def read_single(self) -> Any:
        return self.read().pop(0)

    def add_map(self, f: MapFunc) -> "Input":
        self._pipeline.append(f)
        return self

    def _map(self, item: Any) -> Any:
        curr = item
        for f in self._pipeline:
            curr = f(curr)
        return curr
