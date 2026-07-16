

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemMinMaxType(
    enum.StrEnum
):
    """
    Min Max type
    """

    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"

    def visit(self, minimum: typing.Callable[[], T_Result], maximum: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemMinMaxType.MINIMUM
        ):
            return minimum()
        if (
            self
            is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemMinMaxType.MAXIMUM
        ):
            return maximum()
