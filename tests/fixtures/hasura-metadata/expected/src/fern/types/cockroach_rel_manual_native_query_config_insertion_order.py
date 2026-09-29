

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CockroachRelManualNativeQueryConfigInsertionOrder(enum.StrEnum):
    BEFORE_PARENT = "before_parent"
    AFTER_PARENT = "after_parent"

    def visit(
        self, before_parent: typing.Callable[[], T_Result], after_parent: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is CockroachRelManualNativeQueryConfigInsertionOrder.BEFORE_PARENT:
            return before_parent()
        if self is CockroachRelManualNativeQueryConfigInsertionOrder.AFTER_PARENT:
            return after_parent()
