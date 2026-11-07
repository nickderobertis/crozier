

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryPlanKeysNodeDtoType(enum.StrEnum):
    EMPTY = "EMPTY"
    SINGLE = "SINGLE"
    ALL = "ALL"
    SIMPLE = "SIMPLE"
    COMPOSITE = "COMPOSITE"
    CONSTRAINT = "CONSTRAINT"

    def visit(
        self,
        empty: typing.Callable[[], T_Result],
        single: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
        simple: typing.Callable[[], T_Result],
        composite: typing.Callable[[], T_Result],
        constraint: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is QueryPlanKeysNodeDtoType.EMPTY:
            return empty()
        if self is QueryPlanKeysNodeDtoType.SINGLE:
            return single()
        if self is QueryPlanKeysNodeDtoType.ALL:
            return all_()
        if self is QueryPlanKeysNodeDtoType.SIMPLE:
            return simple()
        if self is QueryPlanKeysNodeDtoType.COMPOSITE:
            return composite()
        if self is QueryPlanKeysNodeDtoType.CONSTRAINT:
            return constraint()
