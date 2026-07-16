

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage(
    str, enum.Enum
):
    """
    Refers to which interest rate is applied when interests are tiered. For example, if an overdraft balance is �2k and the interest tiers are:- 0-�500 0.1%, 500-1000 0.2%, 1000-10000 0.5%, then the applicable interest rate could either be 0.5% of the entire balance (since the account balance sits in the top interest tier) or (0.1%*500)+(0.2%*500)+(0.5%*1000). In the 1st situation, we say the interest is applied to the �Whole� of the account balance,  and in the 2nd that it is �Tiered�.
    """

    INBA = "INBA"
    INTI = "INTI"
    INWH = "INWH"

    def visit(
        self,
        inba: typing.Callable[[], T_Result],
        inti: typing.Callable[[], T_Result],
        inwh: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage.INBA
        ):
            return inba()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage.INTI
        ):
            return inti()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage.INWH
        ):
            return inwh()
