

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetActiveQueryQuery(enum.StrEnum):
    IDLE = "idle"
    ACTIVE = "active"

    def visit(self, idle: typing.Callable[[], T_Result], active: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetActiveQueryQuery.IDLE:
            return idle()
        if self is GetActiveQueryQuery.ACTIVE:
            return active()
