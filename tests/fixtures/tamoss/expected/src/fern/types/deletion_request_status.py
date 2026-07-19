

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeletionRequestStatus(enum.StrEnum):
    """
    Status of the delete request
    """

    CREATED = "created"
    STARTED = "started"
    DONE = "done"
    ERROR = "error"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        started: typing.Callable[[], T_Result],
        done: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeletionRequestStatus.CREATED:
            return created()
        if self is DeletionRequestStatus.STARTED:
            return started()
        if self is DeletionRequestStatus.DONE:
            return done()
        if self is DeletionRequestStatus.ERROR:
            return error()
