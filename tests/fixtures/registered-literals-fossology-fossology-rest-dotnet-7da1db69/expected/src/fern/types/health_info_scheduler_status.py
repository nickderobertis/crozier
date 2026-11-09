

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthInfoSchedulerStatus(enum.StrEnum):
    """
    Health status of scheduler
    """

    OK = "OK"
    ERROR = "ERROR"

    def visit(self, ok: typing.Callable[[], T_Result], error: typing.Callable[[], T_Result]) -> T_Result:
        if self is HealthInfoSchedulerStatus.OK:
            return ok()
        if self is HealthInfoSchedulerStatus.ERROR:
            return error()
