

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FleetUiMessageChunkFinishFinishReason(enum.StrEnum):
    STOP = "stop"
    ERROR = "error"

    def visit(self, stop: typing.Callable[[], T_Result], error: typing.Callable[[], T_Result]) -> T_Result:
        if self is FleetUiMessageChunkFinishFinishReason.STOP:
            return stop()
        if self is FleetUiMessageChunkFinishFinishReason.ERROR:
            return error()
