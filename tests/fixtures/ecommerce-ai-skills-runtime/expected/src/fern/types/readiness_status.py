

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReadinessStatus(enum.StrEnum):
    READY = "ready"
    NOT_READY = "not_ready"

    def visit(self, ready: typing.Callable[[], T_Result], not_ready: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReadinessStatus.READY:
            return ready()
        if self is ReadinessStatus.NOT_READY:
            return not_ready()
