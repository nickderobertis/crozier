

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GroupSyncResultStatus(enum.StrEnum):
    SUCCESS = "success"
    FAILURE = "failure"

    def visit(self, success: typing.Callable[[], T_Result], failure: typing.Callable[[], T_Result]) -> T_Result:
        if self is GroupSyncResultStatus.SUCCESS:
            return success()
        if self is GroupSyncResultStatus.FAILURE:
            return failure()
