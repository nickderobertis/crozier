

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetUpdateJobRequestOperation(enum.StrEnum):
    UPDATE_JOB = "UpdateJob"

    def visit(self, update_job: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetUpdateJobRequestOperation.UPDATE_JOB:
            return update_job()
