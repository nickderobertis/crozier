

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage(enum.StrEnum):
    """
    Refers to which interest rate is applied when interests are tiered. For example, if an overdraft balance is £2k and the interest tiers are:- 0-£500 0.1%, 500-1000 0.2%, 1000-10000 0.5%, then the applicable interest rate could either be 0.5% of the entire balance (since the account balance sits in the top interest tier) or (0.1%*500)+(0.2%*500)+(0.5%*1000). In the 1st situation, we say the interest is applied to the ‘Whole’ of the account balance,  and in the 2nd that it is ‘Tiered’.
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
        if (
            self
            is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage.BANDED
        ):
            return banded()
        if (
            self
            is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage.TIERED
        ):
            return tiered()
        if (
            self
            is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage.WHOLE
        ):
            return whole()
