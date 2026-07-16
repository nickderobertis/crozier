

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemTierBandMethod(
    str, enum.Enum
):
    """
    The methodology of how credit interest is charged. It can be:-
    1. Banded
    Interest rates are banded. i.e. Increasing rate on whole balance as balance increases.
    2. Tiered
    Interest rates are tiered. i.e. increasing rate for each tier as balance increases, but interest paid on tier fixed for that tier and not on whole balance.
    3. Whole
    The same interest rate is applied irrespective of the SME Loan balance
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
            is ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemTierBandMethod.INBA
        ):
            return inba()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemTierBandMethod.INTI
        ):
            return inti()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemTierBandMethod.INWH
        ):
            return inwh()
