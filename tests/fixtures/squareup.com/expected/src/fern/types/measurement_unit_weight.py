

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MeasurementUnitWeight(enum.StrEnum):
    """
    Unit of weight used to measure a quantity.
    """

    IMPERIAL_WEIGHT_OUNCE = "IMPERIAL_WEIGHT_OUNCE"
    IMPERIAL_POUND = "IMPERIAL_POUND"
    IMPERIAL_STONE = "IMPERIAL_STONE"
    METRIC_MILLIGRAM = "METRIC_MILLIGRAM"
    METRIC_GRAM = "METRIC_GRAM"
    METRIC_KILOGRAM = "METRIC_KILOGRAM"

    def visit(
        self,
        imperial_weight_ounce: typing.Callable[[], T_Result],
        imperial_pound: typing.Callable[[], T_Result],
        imperial_stone: typing.Callable[[], T_Result],
        metric_milligram: typing.Callable[[], T_Result],
        metric_gram: typing.Callable[[], T_Result],
        metric_kilogram: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MeasurementUnitWeight.IMPERIAL_WEIGHT_OUNCE:
            return imperial_weight_ounce()
        if self is MeasurementUnitWeight.IMPERIAL_POUND:
            return imperial_pound()
        if self is MeasurementUnitWeight.IMPERIAL_STONE:
            return imperial_stone()
        if self is MeasurementUnitWeight.METRIC_MILLIGRAM:
            return metric_milligram()
        if self is MeasurementUnitWeight.METRIC_GRAM:
            return metric_gram()
        if self is MeasurementUnitWeight.METRIC_KILOGRAM:
            return metric_kilogram()
