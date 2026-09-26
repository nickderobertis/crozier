

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileMessageType(enum.StrEnum):
    """
    The type of message to send. You must provide `file` in this field
    """

    FILE = "file"

    def visit(self, file: typing.Callable[[], T_Result]) -> T_Result:
        if self is FileMessageType.FILE:
            return file()
