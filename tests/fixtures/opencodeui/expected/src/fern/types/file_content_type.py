

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileContentType(enum.StrEnum):
    TEXT = "text"

    def visit(self, text: typing.Callable[[], T_Result]) -> T_Result:
        if self is FileContentType.TEXT:
            return text()
