

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObbcaData1CreditInterestTierBandSetItemTierBandItemFixedVariableInterestRateType(str, enum.Enum):
    """
    Type of interest rate, Fixed or Variable
    """

    FIXED = "Fixed"
    VARIABLE = "Variable"

    def visit(self, fixed: typing.Callable[[], T_Result], variable: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObbcaData1CreditInterestTierBandSetItemTierBandItemFixedVariableInterestRateType.FIXED:
            return fixed()
        if self is ObbcaData1CreditInterestTierBandSetItemTierBandItemFixedVariableInterestRateType.VARIABLE:
            return variable()
