

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeTypes9(enum.StrEnum):
    SINK = "Sink"

    def visit(self, sink: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodeTypes9.SINK:
            return sink()
