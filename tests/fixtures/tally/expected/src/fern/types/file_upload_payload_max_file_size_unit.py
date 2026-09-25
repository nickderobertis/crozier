

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileUploadPayloadMaxFileSizeUnit(enum.StrEnum):
    """
    Unit for maxFileSize. Required when hasMaxFileSize is true.
    """

    KB = "KB"
    MB = "MB"
    GB = "GB"

    def visit(
        self, kb: typing.Callable[[], T_Result], mb: typing.Callable[[], T_Result], gb: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is FileUploadPayloadMaxFileSizeUnit.KB:
            return kb()
        if self is FileUploadPayloadMaxFileSizeUnit.MB:
            return mb()
        if self is FileUploadPayloadMaxFileSizeUnit.GB:
            return gb()
