

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchDocumentOp(enum.StrEnum):
    """
    The operation to be performed
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
        if self is PatchDocumentOp.ADD:
            return add()
        if self is PatchDocumentOp.REMOVE:
            return remove()
        if self is PatchDocumentOp.REPLACE:
            return replace()
        if self is PatchDocumentOp.MOVE:
            return move()
        if self is PatchDocumentOp.COPY:
            return copy()
        if self is PatchDocumentOp.TEST:
            return test()
