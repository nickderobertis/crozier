

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetListJobsRequestOperation(enum.StrEnum):
    LIST_JOBS = "ListJobs"

    def visit(self, list_jobs: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetListJobsRequestOperation.LIST_JOBS:
            return list_jobs()
