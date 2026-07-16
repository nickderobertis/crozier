

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObbcaData1CreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage(str, enum.Enum):
    """
    Amount on which Interest applied.
    """

    BANDED = "Banded"
    TIERED = "Tiered"
    WHOLE = "Whole"

    def visit(
        self,
        banded: typing.Callable[[], T_Result],
        tiered: typing.Callable[[], T_Result],
        whole: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObbcaData1CreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage.BANDED:
            return banded()
        if self is ObbcaData1CreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage.TIERED:
            return tiered()
        if self is ObbcaData1CreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage.WHOLE:
            return whole()
