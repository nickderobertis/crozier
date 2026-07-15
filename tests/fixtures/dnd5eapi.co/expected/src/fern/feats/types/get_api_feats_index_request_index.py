

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetApiFeatsIndexRequestIndex(str, enum.Enum):
    GRAPPLER = "grappler"

    def visit(self, grappler: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetApiFeatsIndexRequestIndex.GRAPPLER:
            return grappler()
