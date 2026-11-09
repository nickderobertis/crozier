

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConfResponseType(enum.StrEnum):
    """
    Denotes if info was created on error
    """

    INFO = "INFO"
    ERROR = "ERROR"

    def visit(self, info: typing.Callable[[], T_Result], error: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConfResponseType.INFO:
            return info()
        if self is ConfResponseType.ERROR:
            return error()
