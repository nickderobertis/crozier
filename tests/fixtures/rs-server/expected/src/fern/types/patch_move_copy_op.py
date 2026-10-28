

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchMoveCopyOp(enum.StrEnum):
    MOVE = "move"
    COPY = "copy"

    def visit(self, move: typing.Callable[[], T_Result], copy: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchMoveCopyOp.MOVE:
            return move()
        if self is PatchMoveCopyOp.COPY:
            return copy()
