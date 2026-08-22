

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UntagResource20161125RequestOperation(enum.StrEnum):
    UNTAG = "Untag"

    def visit(self, untag: typing.Callable[[], T_Result]) -> T_Result:
        if self is UntagResource20161125RequestOperation.UNTAG:
            return untag()
