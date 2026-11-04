

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeTypes3(enum.StrEnum):
    FILTER = "Filter"

    def visit(self, filter: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodeTypes3.FILTER:
            return filter()
