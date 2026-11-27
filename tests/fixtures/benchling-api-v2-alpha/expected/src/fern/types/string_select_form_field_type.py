

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StringSelectFormFieldType(enum.StrEnum):
    """
    The type of this form field. Type declares how this field behaves and dictates the additional properties passed along with the required properties like label and key
    """

    STRING_SELECTION = "STRING_SELECTION"

    def visit(self, string_selection: typing.Callable[[], T_Result]) -> T_Result:
        if self is StringSelectFormFieldType.STRING_SELECTION:
            return string_selection()
