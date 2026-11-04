

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UploadState(enum.StrEnum):
    OPEN = "open"
    COMPLETING = "completing"
    COMPLETED = "completed"
    ABORTED = "aborted"
    EXPIRED = "expired"

    def visit(
        self,
        open: typing.Callable[[], T_Result],
        completing: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        aborted: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UploadState.OPEN:
            return open()
        if self is UploadState.COMPLETING:
            return completing()
        if self is UploadState.COMPLETED:
            return completed()
        if self is UploadState.ABORTED:
            return aborted()
        if self is UploadState.EXPIRED:
            return expired()
