

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObpcaData1CreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage(str, enum.Enum):
    """
    Amount on which Interest applied.
    """

    TIERED = "Tiered"
    WHOLE = "Whole"

    def visit(self, tiered: typing.Callable[[], T_Result], whole: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObpcaData1CreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage.TIERED:
            return tiered()
        if self is ObpcaData1CreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage.WHOLE:
            return whole()
