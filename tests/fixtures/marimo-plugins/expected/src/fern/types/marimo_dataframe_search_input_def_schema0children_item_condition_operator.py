

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator(enum.StrEnum):
    """
    {"label":" "}
    """

    IS_TRUE = "is_true"
    IS_FALSE = "is_false"
    EQUAL_TO = "=="
    NOT_EQUALS = "!="
    GREATER_THAN = ">"
    GREATER_THAN_OR_EQUAL_TO = ">="
    LESS_THAN = "<"
    LESS_THAN_OR_EQUAL_TO = "<="
    BETWEEN = "between"
    IS_NULL = "is_null"
    IS_NOT_NULL = "is_not_null"
    EQUALS = "equals"
    DOES_NOT_EQUAL = "does_not_equal"
    CONTAINS = "contains"
    REGEX = "regex"
    STARTS_WITH = "starts_with"
    ENDS_WITH = "ends_with"
    IN = "in"
    NOT_IN = "not_in"
    IS_EMPTY = "is_empty"

    def visit(
        self,
        is_true: typing.Callable[[], T_Result],
        is_false: typing.Callable[[], T_Result],
        equal_to: typing.Callable[[], T_Result],
        not_equals: typing.Callable[[], T_Result],
        greater_than: typing.Callable[[], T_Result],
        greater_than_or_equal_to: typing.Callable[[], T_Result],
        less_than: typing.Callable[[], T_Result],
        less_than_or_equal_to: typing.Callable[[], T_Result],
        between: typing.Callable[[], T_Result],
        is_null: typing.Callable[[], T_Result],
        is_not_null: typing.Callable[[], T_Result],
        equals: typing.Callable[[], T_Result],
        does_not_equal: typing.Callable[[], T_Result],
        contains: typing.Callable[[], T_Result],
        regex: typing.Callable[[], T_Result],
        starts_with: typing.Callable[[], T_Result],
        ends_with: typing.Callable[[], T_Result],
        in_: typing.Callable[[], T_Result],
        not_in: typing.Callable[[], T_Result],
        is_empty: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.IS_TRUE:
            return is_true()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.IS_FALSE:
            return is_false()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.EQUAL_TO:
            return equal_to()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.NOT_EQUALS:
            return not_equals()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.GREATER_THAN:
            return greater_than()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.GREATER_THAN_OR_EQUAL_TO:
            return greater_than_or_equal_to()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.LESS_THAN:
            return less_than()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.LESS_THAN_OR_EQUAL_TO:
            return less_than_or_equal_to()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.BETWEEN:
            return between()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.IS_NULL:
            return is_null()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.IS_NOT_NULL:
            return is_not_null()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.EQUALS:
            return equals()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.DOES_NOT_EQUAL:
            return does_not_equal()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.CONTAINS:
            return contains()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.REGEX:
            return regex()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.STARTS_WITH:
            return starts_with()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.ENDS_WITH:
            return ends_with()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.IN:
            return in_()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.NOT_IN:
            return not_in()
        if self is MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator.IS_EMPTY:
            return is_empty()
