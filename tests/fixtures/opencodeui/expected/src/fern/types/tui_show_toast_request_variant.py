

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TuiShowToastRequestVariant(enum.StrEnum):
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"

    def visit(
        self,
        info: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        warning: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TuiShowToastRequestVariant.INFO:
            return info()
        if self is TuiShowToastRequestVariant.SUCCESS:
            return success()
        if self is TuiShowToastRequestVariant.WARNING:
            return warning()
        if self is TuiShowToastRequestVariant.ERROR:
            return error()
