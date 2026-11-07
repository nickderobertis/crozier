

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthInfoDbStatus(enum.StrEnum):
    """
    Health status of DB connection
    """

    OK = "OK"
    ERROR = "ERROR"

    def visit(self, ok: typing.Callable[[], T_Result], error: typing.Callable[[], T_Result]) -> T_Result:
        if self is HealthInfoDbStatus.OK:
            return ok()
        if self is HealthInfoDbStatus.ERROR:
            return error()
