

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ShelfType(enum.StrEnum):
    """
    Mounted on the wall.
    """

    WALL = "wall"

    def visit(self, wall: typing.Callable[[], T_Result]) -> T_Result:
        if self is ShelfType.WALL:
            return wall()
