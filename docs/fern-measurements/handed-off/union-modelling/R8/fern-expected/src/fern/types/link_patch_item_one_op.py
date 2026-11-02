

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LinkPatchItemOneOp(enum.StrEnum):
    """
    What to do with one link.
    """

    ADD = "add"
    REMOVE = "remove"

    def visit(self, add: typing.Callable[[], T_Result], remove: typing.Callable[[], T_Result]) -> T_Result:
        if self is LinkPatchItemOneOp.ADD:
            return add()
        if self is LinkPatchItemOneOp.REMOVE:
            return remove()
