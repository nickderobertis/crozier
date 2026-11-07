

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MonitorConditionType(enum.StrEnum):
    """
    A comparison operation to apply to the value selected by the source_selector [greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to]
    """

    GREATER_THAN = "greater_than"
    GREATER_THAN_OR_EQUAL_TO = "greater_than_or_equal_to"
    LESS_THAN = "less_than"
    LESS_THAN_OR_EQUAL_TO = "less_than_or_equal_to"
    EQUAL_TO = "equal_to"
    NOT_EQUAL_TO = "not_equal_to"
    COUNT = "count"

    def visit(
        self,
        greater_than: typing.Callable[[], T_Result],
        greater_than_or_equal_to: typing.Callable[[], T_Result],
        less_than: typing.Callable[[], T_Result],
        less_than_or_equal_to: typing.Callable[[], T_Result],
        equal_to: typing.Callable[[], T_Result],
        not_equal_to: typing.Callable[[], T_Result],
        count: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MonitorConditionType.GREATER_THAN:
            return greater_than()
        if self is MonitorConditionType.GREATER_THAN_OR_EQUAL_TO:
            return greater_than_or_equal_to()
        if self is MonitorConditionType.LESS_THAN:
            return less_than()
        if self is MonitorConditionType.LESS_THAN_OR_EQUAL_TO:
            return less_than_or_equal_to()
        if self is MonitorConditionType.EQUAL_TO:
            return equal_to()
        if self is MonitorConditionType.NOT_EQUAL_TO:
            return not_equal_to()
        if self is MonitorConditionType.COUNT:
            return count()
