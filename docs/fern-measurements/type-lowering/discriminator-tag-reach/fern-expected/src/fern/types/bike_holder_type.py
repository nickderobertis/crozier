

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BikeHolderType(enum.StrEnum):
    BICYCLE = "BICYCLE"

    def visit(self, bicycle: typing.Callable[[], T_Result]) -> T_Result:
        if self is BikeHolderType.BICYCLE:
            return bicycle()
