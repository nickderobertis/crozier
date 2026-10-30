

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FieldDatatypeDisplay(enum.StrEnum):
    """
    Only applicable for select_single: the desired display (select, radio)
    """

    SELECT = "select"
    RADIO = "radio"

    def visit(self, select: typing.Callable[[], T_Result], radio: typing.Callable[[], T_Result]) -> T_Result:
        if self is FieldDatatypeDisplay.SELECT:
            return select()
        if self is FieldDatatypeDisplay.RADIO:
            return radio()
