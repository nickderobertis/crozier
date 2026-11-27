

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConnectionFilesPaginatedListConnectionFilesItemStatus(enum.StrEnum):
    NOT_UPLOADED = "NOT_UPLOADED"
    UPLOADED = "UPLOADED"
    ARCHIVED = "ARCHIVED"
    ERRORED = "ERRORED"
    FORMAT_ERROR = "FORMAT_ERROR"

    def visit(
        self,
        not_uploaded: typing.Callable[[], T_Result],
        uploaded: typing.Callable[[], T_Result],
        archived: typing.Callable[[], T_Result],
        errored: typing.Callable[[], T_Result],
        format_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConnectionFilesPaginatedListConnectionFilesItemStatus.NOT_UPLOADED:
            return not_uploaded()
        if self is ConnectionFilesPaginatedListConnectionFilesItemStatus.UPLOADED:
            return uploaded()
        if self is ConnectionFilesPaginatedListConnectionFilesItemStatus.ARCHIVED:
            return archived()
        if self is ConnectionFilesPaginatedListConnectionFilesItemStatus.ERRORED:
            return errored()
        if self is ConnectionFilesPaginatedListConnectionFilesItemStatus.FORMAT_ERROR:
            return format_error()
