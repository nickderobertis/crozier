

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InfoType(enum.StrEnum):
    """
    Denotes if info was created on error
    """

    INFO = "INFO"
    ERROR = "ERROR"

    def visit(self, info: typing.Callable[[], T_Result], error: typing.Callable[[], T_Result]) -> T_Result:
        if self is InfoType.INFO:
            return info()
        if self is InfoType.ERROR:
            return error()
