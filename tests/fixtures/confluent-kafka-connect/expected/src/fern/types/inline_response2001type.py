

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InlineResponse2001Type(enum.StrEnum):
    """
    Type of connector, sink or source.
    """

    SINK = "sink"
    SOURCE = "source"

    def visit(self, sink: typing.Callable[[], T_Result], source: typing.Callable[[], T_Result]) -> T_Result:
        if self is InlineResponse2001Type.SINK:
            return sink()
        if self is InlineResponse2001Type.SOURCE:
            return source()
