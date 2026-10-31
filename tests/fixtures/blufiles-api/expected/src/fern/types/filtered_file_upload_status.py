

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FilteredFileUploadStatus(enum.StrEnum):
    PENDING = "pending"
    UPLOADING = "uploading"
    COMPLETED = "completed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        uploading: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FilteredFileUploadStatus.PENDING:
            return pending()
        if self is FilteredFileUploadStatus.UPLOADING:
            return uploading()
        if self is FilteredFileUploadStatus.COMPLETED:
            return completed()
