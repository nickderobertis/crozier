

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateInventoryRequestInventoryType(enum.StrEnum):
    """
    infinite or finite
    """

    INFINITE = "infinite"
    FINITE = "finite"

    def visit(self, infinite: typing.Callable[[], T_Result], finite: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateInventoryRequestInventoryType.INFINITE:
            return infinite()
        if self is UpdateInventoryRequestInventoryType.FINITE:
            return finite()
