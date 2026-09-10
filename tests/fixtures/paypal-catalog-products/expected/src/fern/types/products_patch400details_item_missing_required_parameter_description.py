

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProductsPatch400DetailsItemMissingRequiredParameterDescription(enum.StrEnum):
    A_REQUIRED_FIELD_IS_MISSING = "A required field is missing."

    def visit(self, a_required_field_is_missing: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProductsPatch400DetailsItemMissingRequiredParameterDescription.A_REQUIRED_FIELD_IS_MISSING:
            return a_required_field_is_missing()
