

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateResponseBodyTruncation(enum.StrEnum):
    """
    Controls how the service truncates the input when it exceeds the model context window.
    """

    AUTO = "auto"
    DISABLED = "disabled"

    def visit(self, auto: typing.Callable[[], T_Result], disabled: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateResponseBodyTruncation.AUTO:
            return auto()
        if self is CreateResponseBodyTruncation.DISABLED:
            return disabled()
