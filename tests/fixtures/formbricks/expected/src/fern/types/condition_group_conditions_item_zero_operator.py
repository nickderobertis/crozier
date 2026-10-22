

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConditionGroupConditionsItemZeroOperator(enum.StrEnum):
    EQUALS = "equals"
    DOES_NOT_EQUAL = "doesNotEqual"
    CONTAINS = "contains"
    DOES_NOT_CONTAIN = "doesNotContain"
    STARTS_WITH = "startsWith"
    DOES_NOT_START_WITH = "doesNotStartWith"
    ENDS_WITH = "endsWith"
    DOES_NOT_END_WITH = "doesNotEndWith"
    IS_SUBMITTED = "isSubmitted"
    IS_SKIPPED = "isSkipped"
    IS_GREATER_THAN = "isGreaterThan"
    IS_LESS_THAN = "isLessThan"
    IS_GREATER_THAN_OR_EQUAL = "isGreaterThanOrEqual"
    IS_LESS_THAN_OR_EQUAL = "isLessThanOrEqual"
    EQUALS_ONE_OF = "equalsOneOf"
    INCLUDES_ALL_OF = "includesAllOf"
    INCLUDES_ONE_OF = "includesOneOf"
    DOES_NOT_INCLUDE_ONE_OF = "doesNotIncludeOneOf"
    DOES_NOT_INCLUDE_ALL_OF = "doesNotIncludeAllOf"
    IS_CLICKED = "isClicked"
    IS_NOT_CLICKED = "isNotClicked"
    IS_ACCEPTED = "isAccepted"
    IS_BEFORE = "isBefore"
    IS_AFTER = "isAfter"
    IS_BOOKED = "isBooked"
    IS_PARTIALLY_SUBMITTED = "isPartiallySubmitted"
    IS_COMPLETELY_SUBMITTED = "isCompletelySubmitted"
    IS_SET = "isSet"
    IS_NOT_SET = "isNotSet"
    IS_EMPTY = "isEmpty"
    IS_NOT_EMPTY = "isNotEmpty"
    IS_ANY_OF = "isAnyOf"

    def visit(
        self,
        equals: typing.Callable[[], T_Result],
        does_not_equal: typing.Callable[[], T_Result],
        contains: typing.Callable[[], T_Result],
        does_not_contain: typing.Callable[[], T_Result],
        starts_with: typing.Callable[[], T_Result],
        does_not_start_with: typing.Callable[[], T_Result],
        ends_with: typing.Callable[[], T_Result],
        does_not_end_with: typing.Callable[[], T_Result],
        is_submitted: typing.Callable[[], T_Result],
        is_skipped: typing.Callable[[], T_Result],
        is_greater_than: typing.Callable[[], T_Result],
        is_less_than: typing.Callable[[], T_Result],
        is_greater_than_or_equal: typing.Callable[[], T_Result],
        is_less_than_or_equal: typing.Callable[[], T_Result],
        equals_one_of: typing.Callable[[], T_Result],
        includes_all_of: typing.Callable[[], T_Result],
        includes_one_of: typing.Callable[[], T_Result],
        does_not_include_one_of: typing.Callable[[], T_Result],
        does_not_include_all_of: typing.Callable[[], T_Result],
        is_clicked: typing.Callable[[], T_Result],
        is_not_clicked: typing.Callable[[], T_Result],
        is_accepted: typing.Callable[[], T_Result],
        is_before: typing.Callable[[], T_Result],
        is_after: typing.Callable[[], T_Result],
        is_booked: typing.Callable[[], T_Result],
        is_partially_submitted: typing.Callable[[], T_Result],
        is_completely_submitted: typing.Callable[[], T_Result],
        is_set: typing.Callable[[], T_Result],
        is_not_set: typing.Callable[[], T_Result],
        is_empty: typing.Callable[[], T_Result],
        is_not_empty: typing.Callable[[], T_Result],
        is_any_of: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConditionGroupConditionsItemZeroOperator.EQUALS:
            return equals()
        if self is ConditionGroupConditionsItemZeroOperator.DOES_NOT_EQUAL:
            return does_not_equal()
        if self is ConditionGroupConditionsItemZeroOperator.CONTAINS:
            return contains()
        if self is ConditionGroupConditionsItemZeroOperator.DOES_NOT_CONTAIN:
            return does_not_contain()
        if self is ConditionGroupConditionsItemZeroOperator.STARTS_WITH:
            return starts_with()
        if self is ConditionGroupConditionsItemZeroOperator.DOES_NOT_START_WITH:
            return does_not_start_with()
        if self is ConditionGroupConditionsItemZeroOperator.ENDS_WITH:
            return ends_with()
        if self is ConditionGroupConditionsItemZeroOperator.DOES_NOT_END_WITH:
            return does_not_end_with()
        if self is ConditionGroupConditionsItemZeroOperator.IS_SUBMITTED:
            return is_submitted()
        if self is ConditionGroupConditionsItemZeroOperator.IS_SKIPPED:
            return is_skipped()
        if self is ConditionGroupConditionsItemZeroOperator.IS_GREATER_THAN:
            return is_greater_than()
        if self is ConditionGroupConditionsItemZeroOperator.IS_LESS_THAN:
            return is_less_than()
        if self is ConditionGroupConditionsItemZeroOperator.IS_GREATER_THAN_OR_EQUAL:
            return is_greater_than_or_equal()
        if self is ConditionGroupConditionsItemZeroOperator.IS_LESS_THAN_OR_EQUAL:
            return is_less_than_or_equal()
        if self is ConditionGroupConditionsItemZeroOperator.EQUALS_ONE_OF:
            return equals_one_of()
        if self is ConditionGroupConditionsItemZeroOperator.INCLUDES_ALL_OF:
            return includes_all_of()
        if self is ConditionGroupConditionsItemZeroOperator.INCLUDES_ONE_OF:
            return includes_one_of()
        if self is ConditionGroupConditionsItemZeroOperator.DOES_NOT_INCLUDE_ONE_OF:
            return does_not_include_one_of()
        if self is ConditionGroupConditionsItemZeroOperator.DOES_NOT_INCLUDE_ALL_OF:
            return does_not_include_all_of()
        if self is ConditionGroupConditionsItemZeroOperator.IS_CLICKED:
            return is_clicked()
        if self is ConditionGroupConditionsItemZeroOperator.IS_NOT_CLICKED:
            return is_not_clicked()
        if self is ConditionGroupConditionsItemZeroOperator.IS_ACCEPTED:
            return is_accepted()
        if self is ConditionGroupConditionsItemZeroOperator.IS_BEFORE:
            return is_before()
        if self is ConditionGroupConditionsItemZeroOperator.IS_AFTER:
            return is_after()
        if self is ConditionGroupConditionsItemZeroOperator.IS_BOOKED:
            return is_booked()
        if self is ConditionGroupConditionsItemZeroOperator.IS_PARTIALLY_SUBMITTED:
            return is_partially_submitted()
        if self is ConditionGroupConditionsItemZeroOperator.IS_COMPLETELY_SUBMITTED:
            return is_completely_submitted()
        if self is ConditionGroupConditionsItemZeroOperator.IS_SET:
            return is_set()
        if self is ConditionGroupConditionsItemZeroOperator.IS_NOT_SET:
            return is_not_set()
        if self is ConditionGroupConditionsItemZeroOperator.IS_EMPTY:
            return is_empty()
        if self is ConditionGroupConditionsItemZeroOperator.IS_NOT_EMPTY:
            return is_not_empty()
        if self is ConditionGroupConditionsItemZeroOperator.IS_ANY_OF:
            return is_any_of()
