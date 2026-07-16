

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObbcaData1CreditInterestTierBandSetItemCalculationMethod(str, enum.Enum):
    """
    Methods of calculating interest
    """

    COMPOUND = "Compound"
    SIMPLE_INTEREST = "SimpleInterest"

    def visit(
        self, compound: typing.Callable[[], T_Result], simple_interest: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ObbcaData1CreditInterestTierBandSetItemCalculationMethod.COMPOUND:
            return compound()
        if self is ObbcaData1CreditInterestTierBandSetItemCalculationMethod.SIMPLE_INTEREST:
            return simple_interest()
