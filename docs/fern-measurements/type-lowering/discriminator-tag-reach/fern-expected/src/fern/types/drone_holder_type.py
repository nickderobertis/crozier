

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DroneHolderType(enum.StrEnum):
    DRONE = "DRONE"

    def visit(self, drone: typing.Callable[[], T_Result]) -> T_Result:
        if self is DroneHolderType.DRONE:
            return drone()
