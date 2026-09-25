

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SingleConditionalPayloadComparison(enum.StrEnum):
    """
    Comparison operator for the condition.
    """

    IS = "IS"
    IS_NOT = "IS_NOT"
    IS_ANY_OF = "IS_ANY_OF"
    IS_NOT_ANY_OF = "IS_NOT_ANY_OF"
    IS_EVERY_OF = "IS_EVERY_OF"
    CONTAINS = "CONTAINS"
    DOES_NOT_CONTAIN = "DOES_NOT_CONTAIN"
    STARTS_WITH = "STARTS_WITH"
    DOES_NOT_START_WITH = "DOES_NOT_START_WITH"
    ENDS_WITH = "ENDS_WITH"
    DOES_NOT_END_WITH = "DOES_NOT_END_WITH"
    IS_EMPTY = "IS_EMPTY"
    IS_NOT_EMPTY = "IS_NOT_EMPTY"
    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    GREATER_OR_EQUAL_THAN = "GREATER_OR_EQUAL_THAN"
    LESS_OR_EQUAL_THAN = "LESS_OR_EQUAL_THAN"
    IS_BEFORE = "IS_BEFORE"
    IS_AFTER = "IS_AFTER"

    def visit(
        self,
        is_: typing.Callable[[], T_Result],
        is_not: typing.Callable[[], T_Result],
        is_any_of: typing.Callable[[], T_Result],
        is_not_any_of: typing.Callable[[], T_Result],
        is_every_of: typing.Callable[[], T_Result],
        contains: typing.Callable[[], T_Result],
        does_not_contain: typing.Callable[[], T_Result],
        starts_with: typing.Callable[[], T_Result],
        does_not_start_with: typing.Callable[[], T_Result],
        ends_with: typing.Callable[[], T_Result],
        does_not_end_with: typing.Callable[[], T_Result],
        is_empty: typing.Callable[[], T_Result],
        is_not_empty: typing.Callable[[], T_Result],
        equal: typing.Callable[[], T_Result],
        not_equal: typing.Callable[[], T_Result],
        greater_than: typing.Callable[[], T_Result],
        less_than: typing.Callable[[], T_Result],
        greater_or_equal_than: typing.Callable[[], T_Result],
        less_or_equal_than: typing.Callable[[], T_Result],
        is_before: typing.Callable[[], T_Result],
        is_after: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SingleConditionalPayloadComparison.IS:
            return is_()
        if self is SingleConditionalPayloadComparison.IS_NOT:
            return is_not()
        if self is SingleConditionalPayloadComparison.IS_ANY_OF:
            return is_any_of()
        if self is SingleConditionalPayloadComparison.IS_NOT_ANY_OF:
            return is_not_any_of()
        if self is SingleConditionalPayloadComparison.IS_EVERY_OF:
            return is_every_of()
        if self is SingleConditionalPayloadComparison.CONTAINS:
            return contains()
        if self is SingleConditionalPayloadComparison.DOES_NOT_CONTAIN:
            return does_not_contain()
        if self is SingleConditionalPayloadComparison.STARTS_WITH:
            return starts_with()
        if self is SingleConditionalPayloadComparison.DOES_NOT_START_WITH:
            return does_not_start_with()
        if self is SingleConditionalPayloadComparison.ENDS_WITH:
            return ends_with()
        if self is SingleConditionalPayloadComparison.DOES_NOT_END_WITH:
            return does_not_end_with()
        if self is SingleConditionalPayloadComparison.IS_EMPTY:
            return is_empty()
        if self is SingleConditionalPayloadComparison.IS_NOT_EMPTY:
            return is_not_empty()
        if self is SingleConditionalPayloadComparison.EQUAL:
            return equal()
        if self is SingleConditionalPayloadComparison.NOT_EQUAL:
            return not_equal()
        if self is SingleConditionalPayloadComparison.GREATER_THAN:
            return greater_than()
        if self is SingleConditionalPayloadComparison.LESS_THAN:
            return less_than()
        if self is SingleConditionalPayloadComparison.GREATER_OR_EQUAL_THAN:
            return greater_or_equal_than()
        if self is SingleConditionalPayloadComparison.LESS_OR_EQUAL_THAN:
            return less_or_equal_than()
        if self is SingleConditionalPayloadComparison.IS_BEFORE:
            return is_before()
        if self is SingleConditionalPayloadComparison.IS_AFTER:
            return is_after()
