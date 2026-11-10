

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FineTuningJobObject(enum.StrEnum):
    """
    The object type, which is always "fine_tuning.job".
    """

    FINE_TUNING_JOB = "fine_tuning.job"

    def visit(self, fine_tuning_job: typing.Callable[[], T_Result]) -> T_Result:
        if self is FineTuningJobObject.FINE_TUNING_JOB:
            return fine_tuning_job()
