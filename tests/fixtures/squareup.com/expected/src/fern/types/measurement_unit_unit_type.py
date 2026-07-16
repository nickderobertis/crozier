

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MeasurementUnitUnitType(enum.StrEnum):
    """
    Describes the type of this unit and indicates which field contains the unit information. This is an ‘open’ enum.
    """

    TYPE_CUSTOM = "TYPE_CUSTOM"
    TYPE_AREA = "TYPE_AREA"
    TYPE_LENGTH = "TYPE_LENGTH"
    TYPE_VOLUME = "TYPE_VOLUME"
    TYPE_WEIGHT = "TYPE_WEIGHT"
    TYPE_GENERIC = "TYPE_GENERIC"

    def visit(
        self,
        type_custom: typing.Callable[[], T_Result],
        type_area: typing.Callable[[], T_Result],
        type_length: typing.Callable[[], T_Result],
        type_volume: typing.Callable[[], T_Result],
        type_weight: typing.Callable[[], T_Result],
        type_generic: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MeasurementUnitUnitType.TYPE_CUSTOM:
            return type_custom()
        if self is MeasurementUnitUnitType.TYPE_AREA:
            return type_area()
        if self is MeasurementUnitUnitType.TYPE_LENGTH:
            return type_length()
        if self is MeasurementUnitUnitType.TYPE_VOLUME:
            return type_volume()
        if self is MeasurementUnitUnitType.TYPE_WEIGHT:
            return type_weight()
        if self is MeasurementUnitUnitType.TYPE_GENERIC:
            return type_generic()
