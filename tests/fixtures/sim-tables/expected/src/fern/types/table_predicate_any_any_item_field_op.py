

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TablePredicateAnyAnyItemFieldOp(enum.StrEnum):
    """
    Operators: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`; `in`/`nin` take arrays; `isEmpty`, `isNotEmpty`, `isNull`, and `isNotNull` take no operand. Text operators are `contains`, `ncontains`, `startsWith`, `endsWith`, `like`, `nlike`, `ilike`, and `nilike`. Contains variants are case-insensitive and literal; `like`/`nlike` are case-sensitive, while `ilike`/`nilike` are case-insensitive. `*` is the only wildcard; `%`, `_`, and backslash are literal. For `select` columns, single-select accepts `eq`, `ne`, `in`, `nin`; multi-select accepts `contains`, `ncontains`. Option names resolve to IDs.
    """

    EQ = "eq"
    NE = "ne"
    GT = "gt"
    GTE = "gte"
    LT = "lt"
    LTE = "lte"
    IN = "in"
    NIN = "nin"
    CONTAINS = "contains"
    NCONTAINS = "ncontains"
    STARTS_WITH = "startsWith"
    ENDS_WITH = "endsWith"
    LIKE = "like"
    ILIKE = "ilike"
    NLIKE = "nlike"
    NILIKE = "nilike"
    IS_EMPTY = "isEmpty"
    IS_NOT_EMPTY = "isNotEmpty"
    IS_NULL = "isNull"
    IS_NOT_NULL = "isNotNull"

    def visit(
        self,
        eq: typing.Callable[[], T_Result],
        ne: typing.Callable[[], T_Result],
        gt: typing.Callable[[], T_Result],
        gte: typing.Callable[[], T_Result],
        lt: typing.Callable[[], T_Result],
        lte: typing.Callable[[], T_Result],
        in_: typing.Callable[[], T_Result],
        nin: typing.Callable[[], T_Result],
        contains: typing.Callable[[], T_Result],
        ncontains: typing.Callable[[], T_Result],
        starts_with: typing.Callable[[], T_Result],
        ends_with: typing.Callable[[], T_Result],
        like: typing.Callable[[], T_Result],
        ilike: typing.Callable[[], T_Result],
        nlike: typing.Callable[[], T_Result],
        nilike: typing.Callable[[], T_Result],
        is_empty: typing.Callable[[], T_Result],
        is_not_empty: typing.Callable[[], T_Result],
        is_null: typing.Callable[[], T_Result],
        is_not_null: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TablePredicateAnyAnyItemFieldOp.EQ:
            return eq()
        if self is TablePredicateAnyAnyItemFieldOp.NE:
            return ne()
        if self is TablePredicateAnyAnyItemFieldOp.GT:
            return gt()
        if self is TablePredicateAnyAnyItemFieldOp.GTE:
            return gte()
        if self is TablePredicateAnyAnyItemFieldOp.LT:
            return lt()
        if self is TablePredicateAnyAnyItemFieldOp.LTE:
            return lte()
        if self is TablePredicateAnyAnyItemFieldOp.IN:
            return in_()
        if self is TablePredicateAnyAnyItemFieldOp.NIN:
            return nin()
        if self is TablePredicateAnyAnyItemFieldOp.CONTAINS:
            return contains()
        if self is TablePredicateAnyAnyItemFieldOp.NCONTAINS:
            return ncontains()
        if self is TablePredicateAnyAnyItemFieldOp.STARTS_WITH:
            return starts_with()
        if self is TablePredicateAnyAnyItemFieldOp.ENDS_WITH:
            return ends_with()
        if self is TablePredicateAnyAnyItemFieldOp.LIKE:
            return like()
        if self is TablePredicateAnyAnyItemFieldOp.ILIKE:
            return ilike()
        if self is TablePredicateAnyAnyItemFieldOp.NLIKE:
            return nlike()
        if self is TablePredicateAnyAnyItemFieldOp.NILIKE:
            return nilike()
        if self is TablePredicateAnyAnyItemFieldOp.IS_EMPTY:
            return is_empty()
        if self is TablePredicateAnyAnyItemFieldOp.IS_NOT_EMPTY:
            return is_not_empty()
        if self is TablePredicateAnyAnyItemFieldOp.IS_NULL:
            return is_null()
        if self is TablePredicateAnyAnyItemFieldOp.IS_NOT_NULL:
            return is_not_null()
