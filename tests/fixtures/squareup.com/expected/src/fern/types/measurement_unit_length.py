

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MeasurementUnitLength(enum.StrEnum):
    """
    The unit of length used to measure a quantity.
    """

    IMPERIAL_INCH = "IMPERIAL_INCH"
    IMPERIAL_FOOT = "IMPERIAL_FOOT"
    IMPERIAL_YARD = "IMPERIAL_YARD"
    IMPERIAL_MILE = "IMPERIAL_MILE"
    METRIC_MILLIMETER = "METRIC_MILLIMETER"
    METRIC_CENTIMETER = "METRIC_CENTIMETER"
    METRIC_METER = "METRIC_METER"
    METRIC_KILOMETER = "METRIC_KILOMETER"

    def visit(
        self,
        imperial_inch: typing.Callable[[], T_Result],
        imperial_foot: typing.Callable[[], T_Result],
        imperial_yard: typing.Callable[[], T_Result],
        imperial_mile: typing.Callable[[], T_Result],
        metric_millimeter: typing.Callable[[], T_Result],
        metric_centimeter: typing.Callable[[], T_Result],
        metric_meter: typing.Callable[[], T_Result],
        metric_kilometer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MeasurementUnitLength.IMPERIAL_INCH:
            return imperial_inch()
        if self is MeasurementUnitLength.IMPERIAL_FOOT:
            return imperial_foot()
        if self is MeasurementUnitLength.IMPERIAL_YARD:
            return imperial_yard()
        if self is MeasurementUnitLength.IMPERIAL_MILE:
            return imperial_mile()
        if self is MeasurementUnitLength.METRIC_MILLIMETER:
            return metric_millimeter()
        if self is MeasurementUnitLength.METRIC_CENTIMETER:
            return metric_centimeter()
        if self is MeasurementUnitLength.METRIC_METER:
            return metric_meter()
        if self is MeasurementUnitLength.METRIC_KILOMETER:
            return metric_kilometer()
