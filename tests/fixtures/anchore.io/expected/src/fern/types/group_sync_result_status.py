

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GroupSyncResultStatus(str, enum.Enum):
    SUCCESS = "success"
    FAILURE = "failure"

    def visit(self, success: typing.Callable[[], T_Result], failure: typing.Callable[[], T_Result]) -> T_Result:
        if self is GroupSyncResultStatus.SUCCESS:
            return success()
        if self is GroupSyncResultStatus.FAILURE:
            return failure()
