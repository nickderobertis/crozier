

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LinkPatchItemZeroOp(enum.StrEnum):
    """
    What to do with the whole list.
    """

    ADD = "add"
    REPLACE = "replace"

    def visit(self, add: typing.Callable[[], T_Result], replace: typing.Callable[[], T_Result]) -> T_Result:
        if self is LinkPatchItemZeroOp.ADD:
            return add()
        if self is LinkPatchItemZeroOp.REPLACE:
            return replace()
