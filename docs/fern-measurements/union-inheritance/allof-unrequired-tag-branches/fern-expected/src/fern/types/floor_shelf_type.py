

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FloorShelfType(enum.StrEnum):
    """
    Standing on the floor.
    """

    FLOOR = "floor"

    def visit(self, floor: typing.Callable[[], T_Result]) -> T_Result:
        if self is FloorShelfType.FLOOR:
            return floor()
