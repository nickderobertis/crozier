

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MeasurementUnitArea(enum.StrEnum):
    """
    Unit of area used to measure a quantity.
    """

    IMPERIAL_ACRE = "IMPERIAL_ACRE"
    IMPERIAL_SQUARE_INCH = "IMPERIAL_SQUARE_INCH"
    IMPERIAL_SQUARE_FOOT = "IMPERIAL_SQUARE_FOOT"
    IMPERIAL_SQUARE_YARD = "IMPERIAL_SQUARE_YARD"
    IMPERIAL_SQUARE_MILE = "IMPERIAL_SQUARE_MILE"
    METRIC_SQUARE_CENTIMETER = "METRIC_SQUARE_CENTIMETER"
    METRIC_SQUARE_METER = "METRIC_SQUARE_METER"
    METRIC_SQUARE_KILOMETER = "METRIC_SQUARE_KILOMETER"

    def visit(
        self,
        imperial_acre: typing.Callable[[], T_Result],
        imperial_square_inch: typing.Callable[[], T_Result],
        imperial_square_foot: typing.Callable[[], T_Result],
        imperial_square_yard: typing.Callable[[], T_Result],
        imperial_square_mile: typing.Callable[[], T_Result],
        metric_square_centimeter: typing.Callable[[], T_Result],
        metric_square_meter: typing.Callable[[], T_Result],
        metric_square_kilometer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MeasurementUnitArea.IMPERIAL_ACRE:
            return imperial_acre()
        if self is MeasurementUnitArea.IMPERIAL_SQUARE_INCH:
            return imperial_square_inch()
        if self is MeasurementUnitArea.IMPERIAL_SQUARE_FOOT:
            return imperial_square_foot()
        if self is MeasurementUnitArea.IMPERIAL_SQUARE_YARD:
            return imperial_square_yard()
        if self is MeasurementUnitArea.IMPERIAL_SQUARE_MILE:
            return imperial_square_mile()
        if self is MeasurementUnitArea.METRIC_SQUARE_CENTIMETER:
            return metric_square_centimeter()
        if self is MeasurementUnitArea.METRIC_SQUARE_METER:
            return metric_square_meter()
        if self is MeasurementUnitArea.METRIC_SQUARE_KILOMETER:
            return metric_square_kilometer()
