

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FineTuningJobCheckpointObject(enum.StrEnum):
    """
    The object type, which is always "fine_tuning.job.checkpoint".
    """

    FINE_TUNING_JOB_CHECKPOINT = "fine_tuning.job.checkpoint"

    def visit(self, fine_tuning_job_checkpoint: typing.Callable[[], T_Result]) -> T_Result:
        if self is FineTuningJobCheckpointObject.FINE_TUNING_JOB_CHECKPOINT:
            return fine_tuning_job_checkpoint()
