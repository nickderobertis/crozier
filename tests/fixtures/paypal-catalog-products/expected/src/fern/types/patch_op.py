

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchOp(enum.StrEnum):
    """
    The operation.
    """

    ADD = "add"
    REMOVE = "remove"
    REPLACE = "replace"
    MOVE = "move"
    COPY = "copy"
    TEST = "test"

    def visit(
        self,
        add: typing.Callable[[], T_Result],
        remove: typing.Callable[[], T_Result],
        replace: typing.Callable[[], T_Result],
        move: typing.Callable[[], T_Result],
        copy: typing.Callable[[], T_Result],
        test: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatchOp.ADD:
            return add()
        if self is PatchOp.REMOVE:
            return remove()
        if self is PatchOp.REPLACE:
            return replace()
        if self is PatchOp.MOVE:
            return move()
        if self is PatchOp.COPY:
            return copy()
        if self is PatchOp.TEST:
            return test()
