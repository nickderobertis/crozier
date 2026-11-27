

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DateSelectionFormFieldType(enum.StrEnum):
    """
    The type of this form field. Type declares how this field behaves and dictates the additional properties passed along with the required properties like label and key
    """

    DATE_SELECTION = "DATE_SELECTION"

    def visit(self, date_selection: typing.Callable[[], T_Result]) -> T_Result:
        if self is DateSelectionFormFieldType.DATE_SELECTION:
            return date_selection()
