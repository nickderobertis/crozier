

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobStatus(enum.StrEnum):
    """
    The status of the job.
    """

    DRAFT = "draft"
    INTERNAL = "internal"
    PUBLISHED = "published"
    COMPLETED = "completed"
    ON_HOLD = "on-hold"
    PRIVATE = "private"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        internal: typing.Callable[[], T_Result],
        published: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        on_hold: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobStatus.DRAFT:
            return draft()
        if self is JobStatus.INTERNAL:
            return internal()
        if self is JobStatus.PUBLISHED:
            return published()
        if self is JobStatus.COMPLETED:
            return completed()
        if self is JobStatus.ON_HOLD:
            return on_hold()
        if self is JobStatus.PRIVATE:
            return private()
