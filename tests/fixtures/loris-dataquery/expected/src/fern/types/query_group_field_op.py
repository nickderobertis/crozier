

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryGroupFieldOp(enum.StrEnum):
    LT = "lt"
    LTE = "lte"
    EQ = "eq"
    NEQ = "neq"
    GTE = "gte"
    GT = "gt"
    IN = "in"
    STARTS_WITH = "startsWith"
    ENDS_WITH = "endsWith"
    CONTAINS = "contains"
    ISNOTNULL = "isnotnull"
    ISNULL = "isnull"
    EXISTS = "exists"
    NOTEXISTS = "notexists"
    NUMBEROF = "numberof"

    def visit(
        self,
        lt: typing.Callable[[], T_Result],
        lte: typing.Callable[[], T_Result],
        eq: typing.Callable[[], T_Result],
        neq: typing.Callable[[], T_Result],
        gte: typing.Callable[[], T_Result],
        gt: typing.Callable[[], T_Result],
        in_: typing.Callable[[], T_Result],
        starts_with: typing.Callable[[], T_Result],
        ends_with: typing.Callable[[], T_Result],
        contains: typing.Callable[[], T_Result],
        isnotnull: typing.Callable[[], T_Result],
        isnull: typing.Callable[[], T_Result],
        exists: typing.Callable[[], T_Result],
        notexists: typing.Callable[[], T_Result],
        numberof: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is QueryGroupFieldOp.LT:
            return lt()
        if self is QueryGroupFieldOp.LTE:
            return lte()
        if self is QueryGroupFieldOp.EQ:
            return eq()
        if self is QueryGroupFieldOp.NEQ:
            return neq()
        if self is QueryGroupFieldOp.GTE:
            return gte()
        if self is QueryGroupFieldOp.GT:
            return gt()
        if self is QueryGroupFieldOp.IN:
            return in_()
        if self is QueryGroupFieldOp.STARTS_WITH:
            return starts_with()
        if self is QueryGroupFieldOp.ENDS_WITH:
            return ends_with()
        if self is QueryGroupFieldOp.CONTAINS:
            return contains()
        if self is QueryGroupFieldOp.ISNOTNULL:
            return isnotnull()
        if self is QueryGroupFieldOp.ISNULL:
            return isnull()
        if self is QueryGroupFieldOp.EXISTS:
            return exists()
        if self is QueryGroupFieldOp.NOTEXISTS:
            return notexists()
        if self is QueryGroupFieldOp.NUMBEROF:
            return numberof()
