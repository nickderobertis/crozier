

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MeasurementUnitVolume(str, enum.Enum):
    """
    The unit of volume used to measure a quantity.
    """

    GENERIC_FLUID_OUNCE = "GENERIC_FLUID_OUNCE"
    GENERIC_SHOT = "GENERIC_SHOT"
    GENERIC_CUP = "GENERIC_CUP"
    GENERIC_PINT = "GENERIC_PINT"
    GENERIC_QUART = "GENERIC_QUART"
    GENERIC_GALLON = "GENERIC_GALLON"
    IMPERIAL_CUBIC_INCH = "IMPERIAL_CUBIC_INCH"
    IMPERIAL_CUBIC_FOOT = "IMPERIAL_CUBIC_FOOT"
    IMPERIAL_CUBIC_YARD = "IMPERIAL_CUBIC_YARD"
    METRIC_MILLILITER = "METRIC_MILLILITER"
    METRIC_LITER = "METRIC_LITER"

    def visit(
        self,
        generic_fluid_ounce: typing.Callable[[], T_Result],
        generic_shot: typing.Callable[[], T_Result],
        generic_cup: typing.Callable[[], T_Result],
        generic_pint: typing.Callable[[], T_Result],
        generic_quart: typing.Callable[[], T_Result],
        generic_gallon: typing.Callable[[], T_Result],
        imperial_cubic_inch: typing.Callable[[], T_Result],
        imperial_cubic_foot: typing.Callable[[], T_Result],
        imperial_cubic_yard: typing.Callable[[], T_Result],
        metric_milliliter: typing.Callable[[], T_Result],
        metric_liter: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MeasurementUnitVolume.GENERIC_FLUID_OUNCE:
            return generic_fluid_ounce()
        if self is MeasurementUnitVolume.GENERIC_SHOT:
            return generic_shot()
        if self is MeasurementUnitVolume.GENERIC_CUP:
            return generic_cup()
        if self is MeasurementUnitVolume.GENERIC_PINT:
            return generic_pint()
        if self is MeasurementUnitVolume.GENERIC_QUART:
            return generic_quart()
        if self is MeasurementUnitVolume.GENERIC_GALLON:
            return generic_gallon()
        if self is MeasurementUnitVolume.IMPERIAL_CUBIC_INCH:
            return imperial_cubic_inch()
        if self is MeasurementUnitVolume.IMPERIAL_CUBIC_FOOT:
            return imperial_cubic_foot()
        if self is MeasurementUnitVolume.IMPERIAL_CUBIC_YARD:
            return imperial_cubic_yard()
        if self is MeasurementUnitVolume.METRIC_MILLILITER:
            return metric_milliliter()
        if self is MeasurementUnitVolume.METRIC_LITER:
            return metric_liter()
