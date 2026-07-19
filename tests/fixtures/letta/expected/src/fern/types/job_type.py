

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobType(enum.StrEnum):
    JOB = "job"
    RUN = "run"
    BATCH = "batch"

    def visit(
        self,
        job: typing.Callable[[], T_Result],
        run: typing.Callable[[], T_Result],
        batch: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobType.JOB:
            return job()
        if self is JobType.RUN:
            return run()
        if self is JobType.BATCH:
            return batch()
