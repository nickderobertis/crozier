

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeletionReadyResponseDeletionFeedback(enum.StrEnum):
    """
    State of the performed deletion request.
    """

    COMPLETED = "completed"

    def visit(self, completed: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeletionReadyResponseDeletionFeedback.COMPLETED:
            return completed()
