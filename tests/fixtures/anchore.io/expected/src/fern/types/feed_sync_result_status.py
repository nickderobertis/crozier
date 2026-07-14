

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class FeedSyncResultStatus(str, enum.Enum):
    """
    The result of the sync operations, either co
    """

    SUCCESS = "success"
    FAILURE = "failure"

    def visit(self, success: typing.Callable[[], T_Result], failure: typing.Callable[[], T_Result]) -> T_Result:
        if self is FeedSyncResultStatus.SUCCESS:
            return success()
        if self is FeedSyncResultStatus.FAILURE:
            return failure()
