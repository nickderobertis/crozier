

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FieldType(enum.StrEnum):
    """
    The category of a field reference.
    """

    INPUT_FIELD = "INPUT_FIELD"
    CALCULATED_FIELD = "CALCULATED_FIELD"
    HIDDEN_FIELD = "HIDDEN_FIELD"
    UTILITY = "UTILITY"

    def visit(
        self,
        input_field: typing.Callable[[], T_Result],
        calculated_field: typing.Callable[[], T_Result],
        hidden_field: typing.Callable[[], T_Result],
        utility: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FieldType.INPUT_FIELD:
            return input_field()
        if self is FieldType.CALCULATED_FIELD:
            return calculated_field()
        if self is FieldType.HIDDEN_FIELD:
            return hidden_field()
        if self is FieldType.UTILITY:
            return utility()
