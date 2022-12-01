from typing import Any, Callable, Literal

LineType = Literal["multi", "single"]
MapFunc = Callable[[Any], Any]
FilterFunc = Callable[[Any], bool]


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
        self._pipeline = []

    def read(self) -> [Any]:
        with open(self.filepath) as f:
            lines = f.readlines()

        if self._type == "single":
            lines = lines[0].split(self.split_token)

        items = [line.rstrip() for line in lines]
        for (pipe_type, f) in self._pipeline:
            if pipe_type == "map":
                items = [f(item) for item in items]
            elif pipe_type == "filter":
                items = [item for item in items if f(item)]

        return items

    def read_single(self) -> Any:
        return self.read().pop(0)

    def map(self, f: MapFunc) -> "Input":
        self._pipeline.append(("map", f))
        return self

    def filter(self, f: FilterFunc) -> "Input":
        self._pipeline.append(("filter", f))
        return self

    def _map(self, item: Any) -> Any:
        curr = item
        for f in self._pipeline:
            curr = f(curr)
        return curr
