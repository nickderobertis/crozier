

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseFailedStreamingEventResponseTruncation(enum.StrEnum):
    """
    How the input was truncated by the service when it exceeded the model context window.
    """

    AUTO = "auto"
    DISABLED = "disabled"

    def visit(self, auto: typing.Callable[[], T_Result], disabled: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseFailedStreamingEventResponseTruncation.AUTO:
            return auto()
        if self is ResponseFailedStreamingEventResponseTruncation.DISABLED:
            return disabled()
