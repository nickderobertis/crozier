

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileSearchType(enum.StrEnum):
    TEXT = "text"
    REGEX = "regex"

    def visit(self, text: typing.Callable[[], T_Result], regex: typing.Callable[[], T_Result]) -> T_Result:
        if self is FileSearchType.TEXT:
            return text()
        if self is FileSearchType.REGEX:
            return regex()
