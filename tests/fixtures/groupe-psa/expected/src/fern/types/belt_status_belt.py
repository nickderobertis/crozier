

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BeltStatusBelt(enum.StrEnum):
    """
    Belt status.
    """

    NORMAL = "Normal"
    OMISSION = "Omission"

    def visit(self, normal: typing.Callable[[], T_Result], omission: typing.Callable[[], T_Result]) -> T_Result:
        if self is BeltStatusBelt.NORMAL:
            return normal()
        if self is BeltStatusBelt.OMISSION:
            return omission()
