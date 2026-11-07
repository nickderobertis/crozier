

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToolChoiceValueEnum(enum.StrEnum):
    NONE = "none"
    AUTO = "auto"
    REQUIRED = "required"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
        required: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ToolChoiceValueEnum.NONE:
            return none()
        if self is ToolChoiceValueEnum.AUTO:
            return auto()
        if self is ToolChoiceValueEnum.REQUIRED:
            return required()
