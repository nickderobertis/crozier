

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SchedulesListAllRequestStatus(enum.StrEnum):
    ACTIVE = "active"
    PAUSED = "paused"

    def visit(self, active: typing.Callable[[], T_Result], paused: typing.Callable[[], T_Result]) -> T_Result:
        if self is SchedulesListAllRequestStatus.ACTIVE:
            return active()
        if self is SchedulesListAllRequestStatus.PAUSED:
            return paused()
