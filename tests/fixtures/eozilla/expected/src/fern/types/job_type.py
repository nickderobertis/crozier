

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobType(enum.StrEnum):
    PROCESS = "process"

    def visit(self, process: typing.Callable[[], T_Result]) -> T_Result:
        if self is JobType.PROCESS:
            return process()
