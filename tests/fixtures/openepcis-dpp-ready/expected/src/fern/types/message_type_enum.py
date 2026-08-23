

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageTypeEnum(enum.StrEnum):
    """
    Message type (EN 18222 Table 14).
    """

    INFO = "Info"
    WARNING = "Warning"
    ERROR = "Error"
    EXCEPTION = "Exception"

    def visit(
        self,
        info: typing.Callable[[], T_Result],
        warning: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        exception: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MessageTypeEnum.INFO:
            return info()
        if self is MessageTypeEnum.WARNING:
            return warning()
        if self is MessageTypeEnum.ERROR:
            return error()
        if self is MessageTypeEnum.EXCEPTION:
            return exception()
