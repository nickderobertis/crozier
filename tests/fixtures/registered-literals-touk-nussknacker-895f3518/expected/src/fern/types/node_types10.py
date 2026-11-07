

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeTypes10(enum.StrEnum):
    SOURCE = "Source"

    def visit(self, source: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodeTypes10.SOURCE:
            return source()
