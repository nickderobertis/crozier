

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostCancelJobRequestOperation(enum.StrEnum):
    CANCEL_JOB = "CancelJob"

    def visit(self, cancel_job: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostCancelJobRequestOperation.CANCEL_JOB:
            return cancel_job()
