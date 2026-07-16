

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObpcaData1CreditInterestTierBandSetItemTierBandItemBankInterestRateType(str, enum.Enum):
    """
    Interest rate types, other than AER, which financial institutions may use to describe the annual interest rate payable to the PCA.
    """

    LINKED_BASE_RATE = "LinkedBaseRate"
    GROSS = "Gross"
    NET = "Net"
    OTHER = "Other"

    def visit(
        self,
        linked_base_rate: typing.Callable[[], T_Result],
        gross: typing.Callable[[], T_Result],
        net: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObpcaData1CreditInterestTierBandSetItemTierBandItemBankInterestRateType.LINKED_BASE_RATE:
            return linked_base_rate()
        if self is ObpcaData1CreditInterestTierBandSetItemTierBandItemBankInterestRateType.GROSS:
            return gross()
        if self is ObpcaData1CreditInterestTierBandSetItemTierBandItemBankInterestRateType.NET:
            return net()
        if self is ObpcaData1CreditInterestTierBandSetItemTierBandItemBankInterestRateType.OTHER:
            return other()
