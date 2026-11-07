

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StreamProgressStatus(enum.StrEnum):
    """
    Current state, derived from stream_status events.
    """

    NOT_STARTED = "not_started"
    STARTED = "started"
    COMPLETED = "completed"
    SKIPPED = "skipped"
    ERRORED = "errored"

    def visit(
        self,
        not_started: typing.Callable[[], T_Result],
        started: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        skipped: typing.Callable[[], T_Result],
        errored: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StreamProgressStatus.NOT_STARTED:
            return not_started()
        if self is StreamProgressStatus.STARTED:
            return started()
        if self is StreamProgressStatus.COMPLETED:
            return completed()
        if self is StreamProgressStatus.SKIPPED:
            return skipped()
        if self is StreamProgressStatus.ERRORED:
            return errored()
