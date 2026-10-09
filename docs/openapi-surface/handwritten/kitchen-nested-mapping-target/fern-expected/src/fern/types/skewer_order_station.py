

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SkewerOrderStation(enum.StrEnum):
    GRILL = "grill"

    def visit(self, grill: typing.Callable[[], T_Result]) -> T_Result:
        if self is SkewerOrderStation.GRILL:
            return grill()
