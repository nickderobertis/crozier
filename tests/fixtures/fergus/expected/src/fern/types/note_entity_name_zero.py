

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NoteEntityNameZero(enum.StrEnum):
    JOB = "job"

    def visit(self, job: typing.Callable[[], T_Result]) -> T_Result:
        if self is NoteEntityNameZero.JOB:
            return job()
