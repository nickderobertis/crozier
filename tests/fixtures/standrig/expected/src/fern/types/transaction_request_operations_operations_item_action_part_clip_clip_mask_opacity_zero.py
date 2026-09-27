

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionPartClipClipMaskOpacityZero(enum.StrEnum):
    RENDERED = "rendered"

    def visit(self, rendered: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionPartClipClipMaskOpacityZero.RENDERED:
            return rendered()
