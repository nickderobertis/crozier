

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProgressDtoType(enum.StrEnum):
    INFO = "INFO"
    ERROR = "ERROR"
    WARN = "WARN"
    SUCCESS = "SUCCESS"

    def visit(
        self,
        info: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        warn: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProgressDtoType.INFO:
            return info()
        if self is ProgressDtoType.ERROR:
            return error()
        if self is ProgressDtoType.WARN:
            return warn()
        if self is ProgressDtoType.SUCCESS:
            return success()
