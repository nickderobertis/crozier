

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemTariffType(enum.StrEnum):
    """
    TariffType which defines the fee and charges.
    """

    TTEL = "TTEL"
    TTMX = "TTMX"
    TTOT = "TTOT"

    def visit(
        self,
        ttel: typing.Callable[[], T_Result],
        ttmx: typing.Callable[[], T_Result],
        ttot: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemTariffType.TTEL:
            return ttel()
        if self is ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemTariffType.TTMX:
            return ttmx()
        if self is ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemTariffType.TTOT:
            return ttot()
