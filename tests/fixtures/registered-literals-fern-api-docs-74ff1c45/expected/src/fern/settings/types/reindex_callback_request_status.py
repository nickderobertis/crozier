

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ReindexCallbackRequestStatus(enum.StrEnum):
    SUCCESS = "success"
    FAILURE = "failure"

    def visit(self, success: typing.Callable[[], T_Result], failure: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReindexCallbackRequestStatus.SUCCESS:
            return success()
        if self is ReindexCallbackRequestStatus.FAILURE:
            return failure()
