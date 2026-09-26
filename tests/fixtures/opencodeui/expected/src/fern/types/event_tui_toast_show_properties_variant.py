

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventTuiToastShowPropertiesVariant(enum.StrEnum):
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
        if self is EventTuiToastShowPropertiesVariant.INFO:
            return info()
        if self is EventTuiToastShowPropertiesVariant.SUCCESS:
            return success()
        if self is EventTuiToastShowPropertiesVariant.WARNING:
            return warning()
        if self is EventTuiToastShowPropertiesVariant.ERROR:
            return error()
