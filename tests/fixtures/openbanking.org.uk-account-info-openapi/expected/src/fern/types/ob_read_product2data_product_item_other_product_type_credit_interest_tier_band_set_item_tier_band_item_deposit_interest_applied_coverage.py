

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage(
    enum.StrEnum
):
    """
    Amount on which Interest applied.
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
            is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage.INBA
        ):
            return inba()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage.INTI
        ):
            return inti()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage.INWH
        ):
            return inwh()
