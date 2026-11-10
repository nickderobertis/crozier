

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssistantsApiResponseFormatOptionZero(enum.StrEnum):
    """
    `auto` is the default value
    """

    NONE = "none"
    AUTO = "auto"

    def visit(self, none: typing.Callable[[], T_Result], auto: typing.Callable[[], T_Result]) -> T_Result:
        if self is AssistantsApiResponseFormatOptionZero.NONE:
            return none()
        if self is AssistantsApiResponseFormatOptionZero.AUTO:
            return auto()
