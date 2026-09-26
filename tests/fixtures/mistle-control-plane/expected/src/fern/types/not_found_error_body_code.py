

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotFoundErrorBodyCode(enum.StrEnum):
    SNAPSHOT_JOB_NOT_FOUND = "SNAPSHOT_JOB_NOT_FOUND"

    def visit(self, snapshot_job_not_found: typing.Callable[[], T_Result]) -> T_Result:
        if self is NotFoundErrorBodyCode.SNAPSHOT_JOB_NOT_FOUND:
            return snapshot_job_not_found()
