

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType(
    str, enum.Enum
):
    """
    Rate type for overdraft fee/charge (where it is charged in terms of a rate rather than an amount)
    """

    LINKED_BASE_RATE = "LinkedBaseRate"
    GROSS = "Gross"
    NET = "Net"
    OTHER = "Other"

    def visit(
        self,
        linked_base_rate: typing.Callable[[], T_Result],
        gross: typing.Callable[[], T_Result],
        net: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType.LINKED_BASE_RATE
        ):
            return linked_base_rate()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType.GROSS
        ):
            return gross()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType.NET
        ):
            return net()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType.OTHER
        ):
            return other()
