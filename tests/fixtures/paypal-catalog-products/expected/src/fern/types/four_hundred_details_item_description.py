

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FourHundredDetailsItemDescription(enum.StrEnum):
    THE_VALUE_OF_A_FIELD_IS_INVALID = "The value of a field is invalid."

    def visit(self, the_value_of_a_field_is_invalid: typing.Callable[[], T_Result]) -> T_Result:
        if self is FourHundredDetailsItemDescription.THE_VALUE_OF_A_FIELD_IS_INVALID:
            return the_value_of_a_field_is_invalid()
