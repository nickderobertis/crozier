

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SensorTypes(enum.StrEnum):
    """
    An enumeration.
    """

    REFERENCE_GRADE = "reference grade"
    LOW_COST_SENSOR = "low-cost sensor"

    def visit(
        self, reference_grade: typing.Callable[[], T_Result], low_cost_sensor: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is SensorTypes.REFERENCE_GRADE:
            return reference_grade()
        if self is SensorTypes.LOW_COST_SENSOR:
            return low_cost_sensor()
