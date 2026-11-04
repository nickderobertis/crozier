

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AllowedToolsParamMode(enum.StrEnum):
    """
    How to select a tool from the allowed set.
    """

    NONE = "none"
    AUTO = "auto"
    REQUIRED = "required"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
        required: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AllowedToolsParamMode.NONE:
            return none()
        if self is AllowedToolsParamMode.AUTO:
            return auto()
        if self is AllowedToolsParamMode.REQUIRED:
            return required()
