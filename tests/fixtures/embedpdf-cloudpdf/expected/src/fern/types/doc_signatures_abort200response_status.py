

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocSignaturesAbort200ResponseStatus(enum.StrEnum):
    ABORTED = "aborted"
    ALREADY_COMPLETED = "already-completed"
    UNKNOWN = "unknown"

    def visit(
        self,
        aborted: typing.Callable[[], T_Result],
        already_completed: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocSignaturesAbort200ResponseStatus.ABORTED:
            return aborted()
        if self is DocSignaturesAbort200ResponseStatus.ALREADY_COMPLETED:
            return already_completed()
        if self is DocSignaturesAbort200ResponseStatus.UNKNOWN:
            return unknown()
