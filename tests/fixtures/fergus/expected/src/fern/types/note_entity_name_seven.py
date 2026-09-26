

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NoteEntityNameSeven(enum.StrEnum):
    JOB_PHASE = "job_phase"

    def visit(self, job_phase: typing.Callable[[], T_Result]) -> T_Result:
        if self is NoteEntityNameSeven.JOB_PHASE:
            return job_phase()
