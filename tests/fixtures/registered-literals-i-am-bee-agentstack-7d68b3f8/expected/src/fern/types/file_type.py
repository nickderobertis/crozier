

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileType(enum.StrEnum):
    USER_UPLOAD = "user_upload"
    EXTRACTED_TEXT = "extracted_text"

    def visit(
        self, user_upload: typing.Callable[[], T_Result], extracted_text: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is FileType.USER_UPLOAD:
            return user_upload()
        if self is FileType.EXTRACTED_TEXT:
            return extracted_text()
