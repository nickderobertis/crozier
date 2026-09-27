

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HttpLlmResponseChaosTruncateMode(enum.StrEnum):
    NONE = "NONE"
    MID_STREAM = "MID_STREAM"

    def visit(self, none: typing.Callable[[], T_Result], mid_stream: typing.Callable[[], T_Result]) -> T_Result:
        if self is HttpLlmResponseChaosTruncateMode.NONE:
            return none()
        if self is HttpLlmResponseChaosTruncateMode.MID_STREAM:
            return mid_stream()
