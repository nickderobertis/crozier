

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InputTextContentParamType(enum.StrEnum):
    """
    The type of the input item. Always `input_text`.
    """

    INPUT_TEXT = "input_text"

    def visit(self, input_text: typing.Callable[[], T_Result]) -> T_Result:
        if self is InputTextContentParamType.INPUT_TEXT:
            return input_text()
