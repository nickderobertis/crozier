

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NoteReplyEntityNameSeven(enum.StrEnum):
    JOB_PHASE = "job_phase"

    def visit(self, job_phase: typing.Callable[[], T_Result]) -> T_Result:
        if self is NoteReplyEntityNameSeven.JOB_PHASE:
            return job_phase()
