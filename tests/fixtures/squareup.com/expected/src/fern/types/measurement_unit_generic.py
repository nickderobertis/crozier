

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MeasurementUnitGeneric(str, enum.Enum):
    """ """

    UNIT = "UNIT"

    def visit(self, unit: typing.Callable[[], T_Result]) -> T_Result:
        if self is MeasurementUnitGeneric.UNIT:
            return unit()
