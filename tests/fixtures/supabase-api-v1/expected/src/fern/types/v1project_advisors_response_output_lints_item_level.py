

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1ProjectAdvisorsResponseOutputLintsItemLevel(enum.StrEnum):
    ERROR = "ERROR"
    WARN = "WARN"
    INFO = "INFO"

    def visit(
        self,
        error: typing.Callable[[], T_Result],
        warn: typing.Callable[[], T_Result],
        info: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1ProjectAdvisorsResponseOutputLintsItemLevel.ERROR:
            return error()
        if self is V1ProjectAdvisorsResponseOutputLintsItemLevel.WARN:
            return warn()
        if self is V1ProjectAdvisorsResponseOutputLintsItemLevel.INFO:
            return info()
