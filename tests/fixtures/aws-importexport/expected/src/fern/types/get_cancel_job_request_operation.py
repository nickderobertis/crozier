

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetCancelJobRequestOperation(enum.StrEnum):
    CANCEL_JOB = "CancelJob"

    def visit(self, cancel_job: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCancelJobRequestOperation.CANCEL_JOB:
            return cancel_job()
