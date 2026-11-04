

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ValueFilterType(enum.StrEnum):
    CONCEPT = "concept"
    QUANTITY_COMPARATOR = "quantity-comparator"
    QUANTITY_RANGE = "quantity-range"

    def visit(
        self,
        concept: typing.Callable[[], T_Result],
        quantity_comparator: typing.Callable[[], T_Result],
        quantity_range: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ValueFilterType.CONCEPT:
            return concept()
        if self is ValueFilterType.QUANTITY_COMPARATOR:
            return quantity_comparator()
        if self is ValueFilterType.QUANTITY_RANGE:
            return quantity_range()
