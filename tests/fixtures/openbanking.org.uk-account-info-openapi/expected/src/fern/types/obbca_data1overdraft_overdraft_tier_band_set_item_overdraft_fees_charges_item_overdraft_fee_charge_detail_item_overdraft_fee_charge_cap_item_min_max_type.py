

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemMinMaxType(
    str, enum.Enum
):
    """
    Min Max type
    """

    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"

    def visit(self, minimum: typing.Callable[[], T_Result], maximum: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemMinMaxType.MINIMUM
        ):
            return minimum()
        if (
            self
            is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemMinMaxType.MAXIMUM
        ):
            return maximum()
