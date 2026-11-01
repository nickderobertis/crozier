

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TestExecutionsPatchRequestStatusOne(enum.StrEnum):
    COMPLETED = "COMPLETED"

    def visit(self, completed: typing.Callable[[], T_Result]) -> T_Result:
        if self is TestExecutionsPatchRequestStatusOne.COMPLETED:
            return completed()
