

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObbcaData1CreditInterestTierBandSetItemTierBandItemBankInterestRateType(enum.StrEnum):
    """
    Interest rate types, other than AER, which financial institutions may use to describe the annual interest rate payable to the BCA.
    """

    GROSS = "Gross"
    OTHER = "Other"

    def visit(self, gross: typing.Callable[[], T_Result], other: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObbcaData1CreditInterestTierBandSetItemTierBandItemBankInterestRateType.GROSS:
            return gross()
        if self is ObbcaData1CreditInterestTierBandSetItemTierBandItemBankInterestRateType.OTHER:
            return other()
