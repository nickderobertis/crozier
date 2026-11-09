

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FineTuningJobEventObject(enum.StrEnum):
    FINE_TUNING_JOB_EVENT = "fine_tuning.job.event"

    def visit(self, fine_tuning_job_event: typing.Callable[[], T_Result]) -> T_Result:
        if self is FineTuningJobEventObject.FINE_TUNING_JOB_EVENT:
            return fine_tuning_job_event()
