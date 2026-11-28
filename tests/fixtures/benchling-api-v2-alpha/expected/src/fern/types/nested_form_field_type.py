

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NestedFormFieldType(enum.StrEnum):
    """
    The type of this form field. Type declares how this field behaves and dictates the additional properties passed along with the required properties like label and key
    """

    FORM = "FORM"

    def visit(self, form: typing.Callable[[], T_Result]) -> T_Result:
        if self is NestedFormFieldType.FORM:
            return form()
