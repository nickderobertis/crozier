

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Operator(enum.StrEnum):
    GREATER_THAN = "GREATER_THAN"
    GREATER_THAN_OR_EQUAL = "GREATER_THAN_OR_EQUAL"
    LESS_THAN = "LESS_THAN"
    LESS_THAN_OR_EQUAL = "LESS_THAN_OR_EQUAL"
    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"

    def visit(
        self,
        greater_than: typing.Callable[[], T_Result],
        greater_than_or_equal: typing.Callable[[], T_Result],
        less_than: typing.Callable[[], T_Result],
        less_than_or_equal: typing.Callable[[], T_Result],
        equal: typing.Callable[[], T_Result],
        not_equal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Operator.GREATER_THAN:
            return greater_than()
        if self is Operator.GREATER_THAN_OR_EQUAL:
            return greater_than_or_equal()
        if self is Operator.LESS_THAN:
            return less_than()
        if self is Operator.LESS_THAN_OR_EQUAL:
            return less_than_or_equal()
        if self is Operator.EQUAL:
            return equal()
        if self is Operator.NOT_EQUAL:
            return not_equal()
