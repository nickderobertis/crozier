

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CommunicationModelsFieldFilterComparison(enum.StrEnum):
    """
    Optional. The type of value comparison to apply.  Default is Equal.
    """

    EQUAL = "Equal"
    NOT_EQUAL = "NotEqual"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    IN = "In"
    NOT_IN = "NotIn"

    def visit(
        self,
        equal: typing.Callable[[], T_Result],
        not_equal: typing.Callable[[], T_Result],
        less_than: typing.Callable[[], T_Result],
        less_than_or_equal: typing.Callable[[], T_Result],
        greater_than: typing.Callable[[], T_Result],
        greater_than_or_equal: typing.Callable[[], T_Result],
        in_: typing.Callable[[], T_Result],
        not_in: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CommunicationModelsFieldFilterComparison.EQUAL:
            return equal()
        if self is CommunicationModelsFieldFilterComparison.NOT_EQUAL:
            return not_equal()
        if self is CommunicationModelsFieldFilterComparison.LESS_THAN:
            return less_than()
        if self is CommunicationModelsFieldFilterComparison.LESS_THAN_OR_EQUAL:
            return less_than_or_equal()
        if self is CommunicationModelsFieldFilterComparison.GREATER_THAN:
            return greater_than()
        if self is CommunicationModelsFieldFilterComparison.GREATER_THAN_OR_EQUAL:
            return greater_than_or_equal()
        if self is CommunicationModelsFieldFilterComparison.IN:
            return in_()
        if self is CommunicationModelsFieldFilterComparison.NOT_IN:
            return not_in()
