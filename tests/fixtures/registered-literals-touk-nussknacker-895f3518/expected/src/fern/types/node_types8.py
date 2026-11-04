

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeTypes8(enum.StrEnum):
    PROCESSOR = "Processor"

    def visit(self, processor: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodeTypes8.PROCESSOR:
            return processor()
