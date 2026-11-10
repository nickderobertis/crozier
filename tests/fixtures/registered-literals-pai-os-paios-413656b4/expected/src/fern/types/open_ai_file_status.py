

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OpenAiFileStatus(enum.StrEnum):
    """
    Deprecated. The current status of the file, which can be either `uploaded`, `processed`, or `error`.
    """

    UPLOADED = "uploaded"
    PROCESSED = "processed"
    ERROR = "error"

    def visit(
        self,
        uploaded: typing.Callable[[], T_Result],
        processed: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OpenAiFileStatus.UPLOADED:
            return uploaded()
        if self is OpenAiFileStatus.PROCESSED:
            return processed()
        if self is OpenAiFileStatus.ERROR:
            return error()
