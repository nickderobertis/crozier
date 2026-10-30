

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetJobsRequestSort(enum.StrEnum):
    LATEST = "latest"
    OLDEST = "oldest"
    AZ = "a-z"
    ZA = "z-a"

    def visit(
        self,
        latest: typing.Callable[[], T_Result],
        oldest: typing.Callable[[], T_Result],
        az: typing.Callable[[], T_Result],
        za: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetJobsRequestSort.LATEST:
            return latest()
        if self is GetJobsRequestSort.OLDEST:
            return oldest()
        if self is GetJobsRequestSort.AZ:
            return az()
        if self is GetJobsRequestSort.ZA:
            return za()
