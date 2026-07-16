

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType(
    str, enum.Enum
):
    """
    Rate type for overdraft fee/charge (where it is charged in terms of a rate rather than an amount)
    """

    GROSS = "Gross"
    OTHER = "Other"

    def visit(self, gross: typing.Callable[[], T_Result], other: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType.GROSS
        ):
            return gross()
        if (
            self
            is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType.OTHER
        ):
            return other()
