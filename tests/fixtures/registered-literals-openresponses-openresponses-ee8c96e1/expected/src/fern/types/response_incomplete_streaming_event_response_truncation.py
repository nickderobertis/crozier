

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseIncompleteStreamingEventResponseTruncation(enum.StrEnum):
    """
    How the input was truncated by the service when it exceeded the model context window.
    """

    AUTO = "auto"
    DISABLED = "disabled"

    def visit(self, auto: typing.Callable[[], T_Result], disabled: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResponseIncompleteStreamingEventResponseTruncation.AUTO:
            return auto()
        if self is ResponseIncompleteStreamingEventResponseTruncation.DISABLED:
            return disabled()
