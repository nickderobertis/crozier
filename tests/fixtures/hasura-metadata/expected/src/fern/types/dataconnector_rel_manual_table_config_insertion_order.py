

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataconnectorRelManualTableConfigInsertionOrder(enum.StrEnum):
    BEFORE_PARENT = "before_parent"
    AFTER_PARENT = "after_parent"

    def visit(
        self, before_parent: typing.Callable[[], T_Result], after_parent: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is DataconnectorRelManualTableConfigInsertionOrder.BEFORE_PARENT:
            return before_parent()
        if self is DataconnectorRelManualTableConfigInsertionOrder.AFTER_PARENT:
            return after_parent()
