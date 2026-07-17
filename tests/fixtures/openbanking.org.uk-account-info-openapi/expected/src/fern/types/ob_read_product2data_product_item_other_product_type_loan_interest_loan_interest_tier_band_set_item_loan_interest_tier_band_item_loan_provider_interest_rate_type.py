

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanProviderInterestRateType(
    enum.StrEnum
):
    """
    Interest rate types, other than APR, which financial institutions may use to describe the annual interest rate payable for the SME Loan.
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
            is ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanProviderInterestRateType.INBB
        ):
            return inbb()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanProviderInterestRateType.INFR
        ):
            return infr()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanProviderInterestRateType.INGR
        ):
            return ingr()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanProviderInterestRateType.INLR
        ):
            return inlr()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanProviderInterestRateType.INNE
        ):
            return inne()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanProviderInterestRateType.INOT
        ):
            return inot()
