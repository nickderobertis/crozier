

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostCreateJobRequestOperation(enum.StrEnum):
    CREATE_JOB = "CreateJob"

    def visit(self, create_job: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostCreateJobRequestOperation.CREATE_JOB:
            return create_job()
