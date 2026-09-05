

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RegisterPhoneNextPageLevel(enum.StrEnum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"

    def visit(
        self,
        info: typing.Callable[[], T_Result],
        warning: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RegisterPhoneNextPageLevel.INFO:
            return info()
        if self is RegisterPhoneNextPageLevel.WARNING:
            return warning()
        if self is RegisterPhoneNextPageLevel.ERROR:
            return error()
