

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MeasurementUnitGeneric(enum.StrEnum):
    """ """

    UNIT = "UNIT"

    def visit(self, unit: typing.Callable[[], T_Result]) -> T_Result:
        if self is MeasurementUnitGeneric.UNIT:
            return unit()
