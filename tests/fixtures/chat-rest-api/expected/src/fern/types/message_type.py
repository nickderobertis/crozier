

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageType(enum.StrEnum):
    TEXT = "text"
    FILE = "file"

    def visit(self, text: typing.Callable[[], T_Result], file: typing.Callable[[], T_Result]) -> T_Result:
        if self is MessageType.TEXT:
            return text()
        if self is MessageType.FILE:
            return file()
