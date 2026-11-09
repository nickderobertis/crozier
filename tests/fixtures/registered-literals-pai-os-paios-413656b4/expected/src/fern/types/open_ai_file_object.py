

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OpenAiFileObject(enum.StrEnum):
    """
    The object type, which is always `file`.
    """

    FILE = "file"

    def visit(self, file: typing.Callable[[], T_Result]) -> T_Result:
        if self is OpenAiFileObject.FILE:
            return file()
