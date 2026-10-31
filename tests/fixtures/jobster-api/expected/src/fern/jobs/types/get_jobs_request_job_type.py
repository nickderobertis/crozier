

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetJobsRequestJobType(enum.StrEnum):
    ALL = "all"
    FULL_TIME = "full-time"
    PART_TIME = "part-time"
    REMOTE = "remote"
    INTERNSHIP = "internship"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        full_time: typing.Callable[[], T_Result],
        part_time: typing.Callable[[], T_Result],
        remote: typing.Callable[[], T_Result],
        internship: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetJobsRequestJobType.ALL:
            return all_()
        if self is GetJobsRequestJobType.FULL_TIME:
            return full_time()
        if self is GetJobsRequestJobType.PART_TIME:
            return part_time()
        if self is GetJobsRequestJobType.REMOTE:
            return remote()
        if self is GetJobsRequestJobType.INTERNSHIP:
            return internship()
