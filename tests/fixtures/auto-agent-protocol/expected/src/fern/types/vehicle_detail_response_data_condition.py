

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VehicleDetailResponseDataCondition(enum.StrEnum):
    """
    Combined condition enum spanning both sale-condition and trade-in-condition vocabularies. For inventory listings and vehicle_of_interest use one of `new` | `used` | `cpo` (Certified Pre-Owned). For trade_in use one of `excellent` | `good` | `fair` | `poor`. The using schema enforces the correct subset by context.
    """

    NEW = "new"
    USED = "used"
    CPO = "cpo"

    def visit(
        self,
        new: typing.Callable[[], T_Result],
        used: typing.Callable[[], T_Result],
        cpo: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VehicleDetailResponseDataCondition.NEW:
            return new()
        if self is VehicleDetailResponseDataCondition.USED:
            return used()
        if self is VehicleDetailResponseDataCondition.CPO:
            return cpo()
