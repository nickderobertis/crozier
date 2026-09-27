

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionDeformerTargetsSetModeOne(enum.StrEnum):
    MERGE = "merge"

    def visit(self, merge: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionDeformerTargetsSetModeOne.MERGE:
            return merge()
