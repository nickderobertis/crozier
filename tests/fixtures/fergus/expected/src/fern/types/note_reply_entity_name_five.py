

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NoteReplyEntityNameFive(enum.StrEnum):
    TASK = "task"

    def visit(self, task: typing.Callable[[], T_Result]) -> T_Result:
        if self is NoteReplyEntityNameFive.TASK:
            return task()
