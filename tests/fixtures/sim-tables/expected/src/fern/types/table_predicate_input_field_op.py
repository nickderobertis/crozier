

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TablePredicateInputFieldOp(enum.StrEnum):
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
        if self is TablePredicateInputFieldOp.EQ:
            return eq()
        if self is TablePredicateInputFieldOp.NE:
            return ne()
        if self is TablePredicateInputFieldOp.GT:
            return gt()
        if self is TablePredicateInputFieldOp.GTE:
            return gte()
        if self is TablePredicateInputFieldOp.LT:
            return lt()
        if self is TablePredicateInputFieldOp.LTE:
            return lte()
        if self is TablePredicateInputFieldOp.IN:
            return in_()
        if self is TablePredicateInputFieldOp.NIN:
            return nin()
        if self is TablePredicateInputFieldOp.CONTAINS:
            return contains()
        if self is TablePredicateInputFieldOp.NCONTAINS:
            return ncontains()
        if self is TablePredicateInputFieldOp.STARTS_WITH:
            return starts_with()
        if self is TablePredicateInputFieldOp.ENDS_WITH:
            return ends_with()
        if self is TablePredicateInputFieldOp.LIKE:
            return like()
        if self is TablePredicateInputFieldOp.ILIKE:
            return ilike()
        if self is TablePredicateInputFieldOp.NLIKE:
            return nlike()
        if self is TablePredicateInputFieldOp.NILIKE:
            return nilike()
        if self is TablePredicateInputFieldOp.IS_EMPTY:
            return is_empty()
        if self is TablePredicateInputFieldOp.IS_NOT_EMPTY:
            return is_not_empty()
        if self is TablePredicateInputFieldOp.IS_NULL:
            return is_null()
        if self is TablePredicateInputFieldOp.IS_NOT_NULL:
            return is_not_null()
