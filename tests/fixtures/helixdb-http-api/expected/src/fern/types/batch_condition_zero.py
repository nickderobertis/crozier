

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BatchConditionZero(enum.StrEnum):
    PREV_NOT_EMPTY = "prev_not_empty"

    def visit(self, prev_not_empty: typing.Callable[[], T_Result]) -> T_Result:
        if self is BatchConditionZero.PREV_NOT_EMPTY:
            return prev_not_empty()
