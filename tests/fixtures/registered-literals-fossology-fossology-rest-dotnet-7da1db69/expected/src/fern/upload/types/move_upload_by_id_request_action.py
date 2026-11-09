

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MoveUploadByIdRequestAction(enum.StrEnum):
    COPY = "copy"
    MOVE = "move"

    def visit(self, copy: typing.Callable[[], T_Result], move: typing.Callable[[], T_Result]) -> T_Result:
        if self is MoveUploadByIdRequestAction.COPY:
            return copy()
        if self is MoveUploadByIdRequestAction.MOVE:
            return move()
