

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CheckConnectionReadStatus(enum.StrEnum):
    SUCCEEDED = "succeeded"
    FAILED = "failed"

    def visit(self, succeeded: typing.Callable[[], T_Result], failed: typing.Callable[[], T_Result]) -> T_Result:
        if self is CheckConnectionReadStatus.SUCCEEDED:
            return succeeded()
        if self is CheckConnectionReadStatus.FAILED:
            return failed()
