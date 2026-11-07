

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssertionOperator(enum.StrEnum):
    CONTAINS = "contains"
    EQUALS = "equals"
    GREATER_THAN = "greaterThan"
    GREATER_THAN_OR_EQUAL = "greaterThanOrEqual"
    HAS_SIZE = "hasSize"
    LESS_THAN = "lessThan"
    LESS_THAN_OR_EQUAL = "lessThanOrEqual"
    MATCHES = "matches"
    NOT_EQUALS = "notEquals"

    def visit(
        self,
        contains: typing.Callable[[], T_Result],
        equals: typing.Callable[[], T_Result],
        greater_than: typing.Callable[[], T_Result],
        greater_than_or_equal: typing.Callable[[], T_Result],
        has_size: typing.Callable[[], T_Result],
        less_than: typing.Callable[[], T_Result],
        less_than_or_equal: typing.Callable[[], T_Result],
        matches: typing.Callable[[], T_Result],
        not_equals: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AssertionOperator.CONTAINS:
            return contains()
        if self is AssertionOperator.EQUALS:
            return equals()
        if self is AssertionOperator.GREATER_THAN:
            return greater_than()
        if self is AssertionOperator.GREATER_THAN_OR_EQUAL:
            return greater_than_or_equal()
        if self is AssertionOperator.HAS_SIZE:
            return has_size()
        if self is AssertionOperator.LESS_THAN:
            return less_than()
        if self is AssertionOperator.LESS_THAN_OR_EQUAL:
            return less_than_or_equal()
        if self is AssertionOperator.MATCHES:
            return matches()
        if self is AssertionOperator.NOT_EQUALS:
            return not_equals()
