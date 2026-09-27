

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadThresholdComparator(enum.StrEnum):
    """
    how the observed per-run value is compared to the threshold
    """

    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL = "LESS_THAN_OR_EQUAL"
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUAL = "GREATER_THAN_OR_EQUAL"

    def visit(
        self,
        less_than: typing.Callable[[], T_Result],
        less_than_or_equal: typing.Callable[[], T_Result],
        greater_than: typing.Callable[[], T_Result],
        greater_than_or_equal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoadThresholdComparator.LESS_THAN:
            return less_than()
        if self is LoadThresholdComparator.LESS_THAN_OR_EQUAL:
            return less_than_or_equal()
        if self is LoadThresholdComparator.GREATER_THAN:
            return greater_than()
        if self is LoadThresholdComparator.GREATER_THAN_OR_EQUAL:
            return greater_than_or_equal()
