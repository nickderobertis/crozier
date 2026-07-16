

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemMinTermPeriod(
    str, enum.Enum
):
    """
    The unit of period (days, weeks, months etc.) of the Minimum Term
    """

    PACT = "PACT"
    PDAY = "PDAY"
    PHYR = "PHYR"
    PMTH = "PMTH"
    PQTR = "PQTR"
    PWEK = "PWEK"
    PYER = "PYER"

    def visit(
        self,
        pact: typing.Callable[[], T_Result],
        pday: typing.Callable[[], T_Result],
        phyr: typing.Callable[[], T_Result],
        pmth: typing.Callable[[], T_Result],
        pqtr: typing.Callable[[], T_Result],
        pwek: typing.Callable[[], T_Result],
        pyer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemMinTermPeriod.PACT
        ):
            return pact()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemMinTermPeriod.PDAY
        ):
            return pday()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemMinTermPeriod.PHYR
        ):
            return phyr()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemMinTermPeriod.PMTH
        ):
            return pmth()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemMinTermPeriod.PQTR
        ):
            return pqtr()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemMinTermPeriod.PWEK
        ):
            return pwek()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemMinTermPeriod.PYER
        ):
            return pyer()
