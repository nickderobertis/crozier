

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MoveFolderByIdRequestAction(enum.StrEnum):
    COPY = "copy"
    MOVE = "move"

    def visit(self, copy: typing.Callable[[], T_Result], move: typing.Callable[[], T_Result]) -> T_Result:
        if self is MoveFolderByIdRequestAction.COPY:
            return copy()
        if self is MoveFolderByIdRequestAction.MOVE:
            return move()
