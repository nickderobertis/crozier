

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LifecycleConditionDtoOperatorType(enum.StrEnum):
    EQUALS = "EQUALS"
    OBJECT_EQUALS = "OBJECT_EQUALS"
    NOT_EQUAL = "NOT_EQUAL"
    IEQUALS = "IEQUALS"
    INOT_EQUAL = "INOT_EQUAL"
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    GREATER_OR_EQUAL = "GREATER_OR_EQUAL"
    LESS_OR_EQUAL = "LESS_OR_EQUAL"
    CONTAINS = "CONTAINS"
    STARTS_WITH = "STARTS_WITH"
    ENDS_WITH = "ENDS_WITH"
    ICONTAINS = "ICONTAINS"
    ISTARTS_WITH = "ISTARTS_WITH"
    IENDS_WITH = "IENDS_WITH"
    NOT_CONTAINS = "NOT_CONTAINS"
    NOT_STARTS_WITH = "NOT_STARTS_WITH"
    NOT_ENDS_WITH = "NOT_ENDS_WITH"
    INOT_CONTAINS = "INOT_CONTAINS"
    INOT_STARTS_WITH = "INOT_STARTS_WITH"
    INOT_ENDS_WITH = "INOT_ENDS_WITH"
    IBETWEEN_INCLUSIVE = "IBETWEEN_INCLUSIVE"
    MATCHES_PATTERN = "MATCHES_PATTERN"
    IMATCHES_PATTERN = "IMATCHES_PATTERN"
    CONTAINS_PATTERN = "CONTAINS_PATTERN"
    STARTS_WITH_PATTERN = "STARTS_WITH_PATTERN"
    ENDS_WITH_PATTERN = "ENDS_WITH_PATTERN"
    ICONTAINS_PATTERN = "ICONTAINS_PATTERN"
    ISTARTS_WITH_PATTERN = "ISTARTS_WITH_PATTERN"
    IENDS_WITH_PATTERN = "IENDS_WITH_PATTERN"
    REGEXP = "REGEXP"
    IREGEXP = "IREGEXP"
    IS_NULL = "IS_NULL"
    NOT_NULL = "NOT_NULL"
    IN_SET = "IN_SET"
    NOT_IN_SET = "NOT_IN_SET"
    EQUALS_FIELD = "EQUALS_FIELD"
    NOT_EQUAL_FIELD = "NOT_EQUAL_FIELD"
    IEQUALS_FIELD = "IEQUALS_FIELD"
    INOT_EQUAL_FIELD = "INOT_EQUAL_FIELD"
    GREATER_THAN_FIELD = "GREATER_THAN_FIELD"
    LESS_THAN_FIELD = "LESS_THAN_FIELD"
    GREATER_OR_EQUAL_FIELD = "GREATER_OR_EQUAL_FIELD"
    LESS_OR_EQUAL_FIELD = "LESS_OR_EQUAL_FIELD"
    CONTAINS_FIELD = "CONTAINS_FIELD"
    STARTS_WITH_FIELD = "STARTS_WITH_FIELD"
    ENDS_WITH_FIELD = "ENDS_WITH_FIELD"
    ICONTAINS_FIELD = "ICONTAINS_FIELD"
    ISTARTS_WITH_FIELD = "ISTARTS_WITH_FIELD"
    IENDS_WITH_FIELD = "IENDS_WITH_FIELD"
    NOT_CONTAINS_FIELD = "NOT_CONTAINS_FIELD"
    NOT_STARTS_WITH_FIELD = "NOT_STARTS_WITH_FIELD"
    NOT_ENDS_WITH_FIELD = "NOT_ENDS_WITH_FIELD"
    INOT_CONTAINS_FIELD = "INOT_CONTAINS_FIELD"
    INOT_STARTS_WITH_FIELD = "INOT_STARTS_WITH_FIELD"
    INOT_ENDS_WITH_FIELD = "INOT_ENDS_WITH_FIELD"
    AND = "AND"
    NOT = "NOT"
    OR = "OR"
    BETWEEN = "BETWEEN"
    BETWEEN_INCLUSIVE = "BETWEEN_INCLUSIVE"
    EQUAL_BY_ATTRIBUTES = "EQUAL_BY_ATTRIBUTES"
    INSTANCE_OF = "INSTANCE_OF"
    LIKE = "LIKE"
    IS_UNCHANGED = "IS_UNCHANGED"
    IS_CHANGED = "IS_CHANGED"

    def visit(
        self,
        equals: typing.Callable[[], T_Result],
        object_equals: typing.Callable[[], T_Result],
        not_equal: typing.Callable[[], T_Result],
        iequals: typing.Callable[[], T_Result],
        inot_equal: typing.Callable[[], T_Result],
        greater_than: typing.Callable[[], T_Result],
        less_than: typing.Callable[[], T_Result],
        greater_or_equal: typing.Callable[[], T_Result],
        less_or_equal: typing.Callable[[], T_Result],
        contains: typing.Callable[[], T_Result],
        starts_with: typing.Callable[[], T_Result],
        ends_with: typing.Callable[[], T_Result],
        icontains: typing.Callable[[], T_Result],
        istarts_with: typing.Callable[[], T_Result],
        iends_with: typing.Callable[[], T_Result],
        not_contains: typing.Callable[[], T_Result],
        not_starts_with: typing.Callable[[], T_Result],
        not_ends_with: typing.Callable[[], T_Result],
        inot_contains: typing.Callable[[], T_Result],
        inot_starts_with: typing.Callable[[], T_Result],
        inot_ends_with: typing.Callable[[], T_Result],
        ibetween_inclusive: typing.Callable[[], T_Result],
        matches_pattern: typing.Callable[[], T_Result],
        imatches_pattern: typing.Callable[[], T_Result],
        contains_pattern: typing.Callable[[], T_Result],
        starts_with_pattern: typing.Callable[[], T_Result],
        ends_with_pattern: typing.Callable[[], T_Result],
        icontains_pattern: typing.Callable[[], T_Result],
        istarts_with_pattern: typing.Callable[[], T_Result],
        iends_with_pattern: typing.Callable[[], T_Result],
        regexp: typing.Callable[[], T_Result],
        iregexp: typing.Callable[[], T_Result],
        is_null: typing.Callable[[], T_Result],
        not_null: typing.Callable[[], T_Result],
        in_set: typing.Callable[[], T_Result],
        not_in_set: typing.Callable[[], T_Result],
        equals_field: typing.Callable[[], T_Result],
        not_equal_field: typing.Callable[[], T_Result],
        iequals_field: typing.Callable[[], T_Result],
        inot_equal_field: typing.Callable[[], T_Result],
        greater_than_field: typing.Callable[[], T_Result],
        less_than_field: typing.Callable[[], T_Result],
        greater_or_equal_field: typing.Callable[[], T_Result],
        less_or_equal_field: typing.Callable[[], T_Result],
        contains_field: typing.Callable[[], T_Result],
        starts_with_field: typing.Callable[[], T_Result],
        ends_with_field: typing.Callable[[], T_Result],
        icontains_field: typing.Callable[[], T_Result],
        istarts_with_field: typing.Callable[[], T_Result],
        iends_with_field: typing.Callable[[], T_Result],
        not_contains_field: typing.Callable[[], T_Result],
        not_starts_with_field: typing.Callable[[], T_Result],
        not_ends_with_field: typing.Callable[[], T_Result],
        inot_contains_field: typing.Callable[[], T_Result],
        inot_starts_with_field: typing.Callable[[], T_Result],
        inot_ends_with_field: typing.Callable[[], T_Result],
        and_: typing.Callable[[], T_Result],
        not_: typing.Callable[[], T_Result],
        or_: typing.Callable[[], T_Result],
        between: typing.Callable[[], T_Result],
        between_inclusive: typing.Callable[[], T_Result],
        equal_by_attributes: typing.Callable[[], T_Result],
        instance_of: typing.Callable[[], T_Result],
        like: typing.Callable[[], T_Result],
        is_unchanged: typing.Callable[[], T_Result],
        is_changed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LifecycleConditionDtoOperatorType.EQUALS:
            return equals()
        if self is LifecycleConditionDtoOperatorType.OBJECT_EQUALS:
            return object_equals()
        if self is LifecycleConditionDtoOperatorType.NOT_EQUAL:
            return not_equal()
        if self is LifecycleConditionDtoOperatorType.IEQUALS:
            return iequals()
        if self is LifecycleConditionDtoOperatorType.INOT_EQUAL:
            return inot_equal()
        if self is LifecycleConditionDtoOperatorType.GREATER_THAN:
            return greater_than()
        if self is LifecycleConditionDtoOperatorType.LESS_THAN:
            return less_than()
        if self is LifecycleConditionDtoOperatorType.GREATER_OR_EQUAL:
            return greater_or_equal()
        if self is LifecycleConditionDtoOperatorType.LESS_OR_EQUAL:
            return less_or_equal()
        if self is LifecycleConditionDtoOperatorType.CONTAINS:
            return contains()
        if self is LifecycleConditionDtoOperatorType.STARTS_WITH:
            return starts_with()
        if self is LifecycleConditionDtoOperatorType.ENDS_WITH:
            return ends_with()
        if self is LifecycleConditionDtoOperatorType.ICONTAINS:
            return icontains()
        if self is LifecycleConditionDtoOperatorType.ISTARTS_WITH:
            return istarts_with()
        if self is LifecycleConditionDtoOperatorType.IENDS_WITH:
            return iends_with()
        if self is LifecycleConditionDtoOperatorType.NOT_CONTAINS:
            return not_contains()
        if self is LifecycleConditionDtoOperatorType.NOT_STARTS_WITH:
            return not_starts_with()
        if self is LifecycleConditionDtoOperatorType.NOT_ENDS_WITH:
            return not_ends_with()
        if self is LifecycleConditionDtoOperatorType.INOT_CONTAINS:
            return inot_contains()
        if self is LifecycleConditionDtoOperatorType.INOT_STARTS_WITH:
            return inot_starts_with()
        if self is LifecycleConditionDtoOperatorType.INOT_ENDS_WITH:
            return inot_ends_with()
        if self is LifecycleConditionDtoOperatorType.IBETWEEN_INCLUSIVE:
            return ibetween_inclusive()
        if self is LifecycleConditionDtoOperatorType.MATCHES_PATTERN:
            return matches_pattern()
        if self is LifecycleConditionDtoOperatorType.IMATCHES_PATTERN:
            return imatches_pattern()
        if self is LifecycleConditionDtoOperatorType.CONTAINS_PATTERN:
            return contains_pattern()
        if self is LifecycleConditionDtoOperatorType.STARTS_WITH_PATTERN:
            return starts_with_pattern()
        if self is LifecycleConditionDtoOperatorType.ENDS_WITH_PATTERN:
            return ends_with_pattern()
        if self is LifecycleConditionDtoOperatorType.ICONTAINS_PATTERN:
            return icontains_pattern()
        if self is LifecycleConditionDtoOperatorType.ISTARTS_WITH_PATTERN:
            return istarts_with_pattern()
        if self is LifecycleConditionDtoOperatorType.IENDS_WITH_PATTERN:
            return iends_with_pattern()
        if self is LifecycleConditionDtoOperatorType.REGEXP:
            return regexp()
        if self is LifecycleConditionDtoOperatorType.IREGEXP:
            return iregexp()
        if self is LifecycleConditionDtoOperatorType.IS_NULL:
            return is_null()
        if self is LifecycleConditionDtoOperatorType.NOT_NULL:
            return not_null()
        if self is LifecycleConditionDtoOperatorType.IN_SET:
            return in_set()
        if self is LifecycleConditionDtoOperatorType.NOT_IN_SET:
            return not_in_set()
        if self is LifecycleConditionDtoOperatorType.EQUALS_FIELD:
            return equals_field()
        if self is LifecycleConditionDtoOperatorType.NOT_EQUAL_FIELD:
            return not_equal_field()
        if self is LifecycleConditionDtoOperatorType.IEQUALS_FIELD:
            return iequals_field()
        if self is LifecycleConditionDtoOperatorType.INOT_EQUAL_FIELD:
            return inot_equal_field()
        if self is LifecycleConditionDtoOperatorType.GREATER_THAN_FIELD:
            return greater_than_field()
        if self is LifecycleConditionDtoOperatorType.LESS_THAN_FIELD:
            return less_than_field()
        if self is LifecycleConditionDtoOperatorType.GREATER_OR_EQUAL_FIELD:
            return greater_or_equal_field()
        if self is LifecycleConditionDtoOperatorType.LESS_OR_EQUAL_FIELD:
            return less_or_equal_field()
        if self is LifecycleConditionDtoOperatorType.CONTAINS_FIELD:
            return contains_field()
        if self is LifecycleConditionDtoOperatorType.STARTS_WITH_FIELD:
            return starts_with_field()
        if self is LifecycleConditionDtoOperatorType.ENDS_WITH_FIELD:
            return ends_with_field()
        if self is LifecycleConditionDtoOperatorType.ICONTAINS_FIELD:
            return icontains_field()
        if self is LifecycleConditionDtoOperatorType.ISTARTS_WITH_FIELD:
            return istarts_with_field()
        if self is LifecycleConditionDtoOperatorType.IENDS_WITH_FIELD:
            return iends_with_field()
        if self is LifecycleConditionDtoOperatorType.NOT_CONTAINS_FIELD:
            return not_contains_field()
        if self is LifecycleConditionDtoOperatorType.NOT_STARTS_WITH_FIELD:
            return not_starts_with_field()
        if self is LifecycleConditionDtoOperatorType.NOT_ENDS_WITH_FIELD:
            return not_ends_with_field()
        if self is LifecycleConditionDtoOperatorType.INOT_CONTAINS_FIELD:
            return inot_contains_field()
        if self is LifecycleConditionDtoOperatorType.INOT_STARTS_WITH_FIELD:
            return inot_starts_with_field()
        if self is LifecycleConditionDtoOperatorType.INOT_ENDS_WITH_FIELD:
            return inot_ends_with_field()
        if self is LifecycleConditionDtoOperatorType.AND:
            return and_()
        if self is LifecycleConditionDtoOperatorType.NOT:
            return not_()
        if self is LifecycleConditionDtoOperatorType.OR:
            return or_()
        if self is LifecycleConditionDtoOperatorType.BETWEEN:
            return between()
        if self is LifecycleConditionDtoOperatorType.BETWEEN_INCLUSIVE:
            return between_inclusive()
        if self is LifecycleConditionDtoOperatorType.EQUAL_BY_ATTRIBUTES:
            return equal_by_attributes()
        if self is LifecycleConditionDtoOperatorType.INSTANCE_OF:
            return instance_of()
        if self is LifecycleConditionDtoOperatorType.LIKE:
            return like()
        if self is LifecycleConditionDtoOperatorType.IS_UNCHANGED:
            return is_unchanged()
        if self is LifecycleConditionDtoOperatorType.IS_CHANGED:
            return is_changed()
