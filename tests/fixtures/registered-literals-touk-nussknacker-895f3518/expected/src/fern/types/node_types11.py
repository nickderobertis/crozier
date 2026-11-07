

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeTypes11(enum.StrEnum):
    SPLIT = "Split"

    def visit(self, split: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodeTypes11.SPLIT:
            return split()
