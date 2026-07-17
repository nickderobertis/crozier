

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObpcaData1CreditInterestTierBandSetItemTierBandItemFixedVariableInterestRateType(enum.StrEnum):
    """
    Type of interest rate, Fixed or Variable
    """

    FIXED = "Fixed"
    VARIABLE = "Variable"

    def visit(self, fixed: typing.Callable[[], T_Result], variable: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObpcaData1CreditInterestTierBandSetItemTierBandItemFixedVariableInterestRateType.FIXED:
            return fixed()
        if self is ObpcaData1CreditInterestTierBandSetItemTierBandItemFixedVariableInterestRateType.VARIABLE:
            return variable()
