

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryStatusStatus(enum.StrEnum):
    READY = "ready"
    BUILDING = "building"

    def visit(self, ready: typing.Callable[[], T_Result], building: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryStatusStatus.READY:
            return ready()
        if self is QueryStatusStatus.BUILDING:
            return building()
