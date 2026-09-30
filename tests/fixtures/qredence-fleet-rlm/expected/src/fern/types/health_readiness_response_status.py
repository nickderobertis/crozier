

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthReadinessResponseStatus(enum.StrEnum):
    READY = "ready"

    def visit(self, ready: typing.Callable[[], T_Result]) -> T_Result:
        if self is HealthReadinessResponseStatus.READY:
            return ready()
