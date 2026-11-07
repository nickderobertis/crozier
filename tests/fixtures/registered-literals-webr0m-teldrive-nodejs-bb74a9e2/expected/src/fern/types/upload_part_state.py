

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UploadPartState(enum.StrEnum):
    RESERVED = "reserved"
    UPLOADING = "uploading"
    STORED = "stored"
    FAILED = "failed"

    def visit(
        self,
        reserved: typing.Callable[[], T_Result],
        uploading: typing.Callable[[], T_Result],
        stored: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UploadPartState.RESERVED:
            return reserved()
        if self is UploadPartState.UPLOADING:
            return uploading()
        if self is UploadPartState.STORED:
            return stored()
        if self is UploadPartState.FAILED:
            return failed()
