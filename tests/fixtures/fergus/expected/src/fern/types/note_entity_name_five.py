

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NoteEntityNameFive(enum.StrEnum):
    TASK = "task"

    def visit(self, task: typing.Callable[[], T_Result]) -> T_Result:
        if self is NoteEntityNameFive.TASK:
            return task()
