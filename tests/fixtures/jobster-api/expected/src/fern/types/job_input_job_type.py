

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobInputJobType(enum.StrEnum):
    FULL_TIME = "full-time"
    PART_TIME = "part-time"
    REMOTE = "remote"
    INTERNSHIP = "internship"

    def visit(
        self,
        full_time: typing.Callable[[], T_Result],
        part_time: typing.Callable[[], T_Result],
        remote: typing.Callable[[], T_Result],
        internship: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobInputJobType.FULL_TIME:
            return full_time()
        if self is JobInputJobType.PART_TIME:
            return part_time()
        if self is JobInputJobType.REMOTE:
            return remote()
        if self is JobInputJobType.INTERNSHIP:
            return internship()
