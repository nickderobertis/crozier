

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlateExtraPlateType(enum.StrEnum):
    KILN = "kiln"

    def visit(self, kiln: typing.Callable[[], T_Result]) -> T_Result:
        if self is PlateExtraPlateType.KILN:
            return kiln()
