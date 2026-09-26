

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VehicleCondition(enum.StrEnum):
    """
    Combined condition enum spanning both sale-condition and trade-in-condition vocabularies. For inventory listings and vehicle_of_interest use one of `new` | `used` | `cpo` (Certified Pre-Owned). For trade_in use one of `excellent` | `good` | `fair` | `poor`. The using schema enforces the correct subset by context.
    """

    NEW = "new"
    USED = "used"
    CPO = "cpo"
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"

    def visit(
        self,
        new: typing.Callable[[], T_Result],
        used: typing.Callable[[], T_Result],
        cpo: typing.Callable[[], T_Result],
        excellent: typing.Callable[[], T_Result],
        good: typing.Callable[[], T_Result],
        fair: typing.Callable[[], T_Result],
        poor: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VehicleCondition.NEW:
            return new()
        if self is VehicleCondition.USED:
            return used()
        if self is VehicleCondition.CPO:
            return cpo()
        if self is VehicleCondition.EXCELLENT:
            return excellent()
        if self is VehicleCondition.GOOD:
            return good()
        if self is VehicleCondition.FAIR:
            return fair()
        if self is VehicleCondition.POOR:
            return poor()
