

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType(
    enum.StrEnum
):
    """
    Rate type for overdraft fee/charge (where it is charged in terms of a rate rather than an amount)
    """

    GROSS = "Gross"
    OTHER = "Other"

    def visit(self, gross: typing.Callable[[], T_Result], other: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType.GROSS
        ):
            return gross()
        if (
            self
            is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType.OTHER
        ):
            return other()
