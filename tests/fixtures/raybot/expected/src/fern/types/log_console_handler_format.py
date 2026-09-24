

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LogConsoleHandlerFormat(enum.StrEnum):
    """
    The log format for the application
    """

    JSON = "JSON"
    TEXT = "TEXT"

    def visit(self, json: typing.Callable[[], T_Result], text: typing.Callable[[], T_Result]) -> T_Result:
        if self is LogConsoleHandlerFormat.JSON:
            return json()
        if self is LogConsoleHandlerFormat.TEXT:
            return text()
