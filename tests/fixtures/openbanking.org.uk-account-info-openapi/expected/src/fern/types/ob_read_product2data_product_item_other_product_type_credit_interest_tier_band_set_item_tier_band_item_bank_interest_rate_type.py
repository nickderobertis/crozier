

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemBankInterestRateType(
    enum.StrEnum
):
    """
    Interest rate types, other than AER, which financial institutions may use to describe the annual interest rate payable to the account holder's account.
    """

    INBB = "INBB"
    INFR = "INFR"
    INGR = "INGR"
    INLR = "INLR"
    INNE = "INNE"
    INOT = "INOT"

    def visit(
        self,
        inbb: typing.Callable[[], T_Result],
        infr: typing.Callable[[], T_Result],
        ingr: typing.Callable[[], T_Result],
        inlr: typing.Callable[[], T_Result],
        inne: typing.Callable[[], T_Result],
        inot: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemBankInterestRateType.INBB
        ):
            return inbb()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemBankInterestRateType.INFR
        ):
            return infr()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemBankInterestRateType.INGR
        ):
            return ingr()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemBankInterestRateType.INLR
        ):
            return inlr()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemBankInterestRateType.INNE
        ):
            return inne()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemBankInterestRateType.INOT
        ):
            return inot()
