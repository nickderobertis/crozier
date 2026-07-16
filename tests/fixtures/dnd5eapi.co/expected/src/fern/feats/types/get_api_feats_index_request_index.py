

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetApiFeatsIndexRequestIndex(enum.StrEnum):
    GRAPPLER = "grappler"

    def visit(self, grappler: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetApiFeatsIndexRequestIndex.GRAPPLER:
            return grappler()
