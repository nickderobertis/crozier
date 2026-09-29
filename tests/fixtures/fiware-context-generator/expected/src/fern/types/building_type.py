

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BuildingType(enum.StrEnum):
    """
    NGSI Entity type
    """

    BUILDING = "Building"

    def visit(self, building: typing.Callable[[], T_Result]) -> T_Result:
        if self is BuildingType.BUILDING:
            return building()
