

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActionState(enum.StrEnum):
    """
    Enum representing the state of the action/activity.
    """

    UNKNOWN = "UNKNOWN"
    ATTEMPT = "ATTEMPT"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    SKIPPED = "SKIPPED"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        attempt: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        failure: typing.Callable[[], T_Result],
        skipped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActionState.UNKNOWN:
            return unknown()
        if self is ActionState.ATTEMPT:
            return attempt()
        if self is ActionState.SUCCESS:
            return success()
        if self is ActionState.FAILURE:
            return failure()
        if self is ActionState.SKIPPED:
            return skipped()
