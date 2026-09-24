

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LogFileHandlerFormat(enum.StrEnum):
    """
    The log format for the application
    """

    JSON = "JSON"
    TEXT = "TEXT"

    def visit(self, json: typing.Callable[[], T_Result], text: typing.Callable[[], T_Result]) -> T_Result:
        if self is LogFileHandlerFormat.JSON:
            return json()
        if self is LogFileHandlerFormat.TEXT:
            return text()
