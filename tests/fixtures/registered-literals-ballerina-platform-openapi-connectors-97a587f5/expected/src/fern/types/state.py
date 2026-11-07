

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class State(enum.StrEnum):
    """
    The state of a job or item.
    """

    NOT_RUNNING = "notRunning"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    CANCELED = "canceled"
    FAILED = "failed"
    DELETED = "deleted"

    def visit(
        self,
        not_running: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is State.NOT_RUNNING:
            return not_running()
        if self is State.RUNNING:
            return running()
        if self is State.SUCCEEDED:
            return succeeded()
        if self is State.CANCELED:
            return canceled()
        if self is State.FAILED:
            return failed()
        if self is State.DELETED:
            return deleted()
