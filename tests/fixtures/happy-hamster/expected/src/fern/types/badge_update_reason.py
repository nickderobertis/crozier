

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BadgeUpdateReason(enum.StrEnum):
    OCCUPANCY = "occupancy"
    NO_UPDATE = "no_update"

    def visit(self, occupancy: typing.Callable[[], T_Result], no_update: typing.Callable[[], T_Result]) -> T_Result:
        if self is BadgeUpdateReason.OCCUPANCY:
            return occupancy()
        if self is BadgeUpdateReason.NO_UPDATE:
            return no_update()
