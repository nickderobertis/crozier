

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SteakOrderStation(enum.StrEnum):
    GRILL = "grill"

    def visit(self, grill: typing.Callable[[], T_Result]) -> T_Result:
        if self is SteakOrderStation.GRILL:
            return grill()
