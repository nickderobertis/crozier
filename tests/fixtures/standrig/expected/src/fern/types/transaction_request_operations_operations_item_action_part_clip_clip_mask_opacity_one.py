

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionPartClipClipMaskOpacityOne(enum.StrEnum):
    IGNORE = "ignore"

    def visit(self, ignore: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionPartClipClipMaskOpacityOne.IGNORE:
            return ignore()
