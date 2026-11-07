

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateUploadByIdRequestStatus(enum.StrEnum):
    OPEN = "Open"
    IN_PROGRESS = "InProgress"
    CLOSED = "Closed"
    REJECTED = "Rejected"

    def visit(
        self,
        open: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        closed: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateUploadByIdRequestStatus.OPEN:
            return open()
        if self is UpdateUploadByIdRequestStatus.IN_PROGRESS:
            return in_progress()
        if self is UpdateUploadByIdRequestStatus.CLOSED:
            return closed()
        if self is UpdateUploadByIdRequestStatus.REJECTED:
            return rejected()
