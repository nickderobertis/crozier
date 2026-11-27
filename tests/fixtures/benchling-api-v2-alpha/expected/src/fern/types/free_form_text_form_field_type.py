

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FreeFormTextFormFieldType(enum.StrEnum):
    """
    The type of this form field. Type declares how this field behaves and dictates the additional properties passed along with the required properties like label and key
    """

    FREE_FORM_TEXT = "FREE_FORM_TEXT"

    def visit(self, free_form_text: typing.Callable[[], T_Result]) -> T_Result:
        if self is FreeFormTextFormFieldType.FREE_FORM_TEXT:
            return free_form_text()
