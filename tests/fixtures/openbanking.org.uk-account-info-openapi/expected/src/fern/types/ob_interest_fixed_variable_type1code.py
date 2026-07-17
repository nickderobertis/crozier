

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObInterestFixedVariableType1Code(enum.StrEnum):
    """
    Type of interest rate, Fixed or Variable
    """

    INFI = "INFI"
    INVA = "INVA"

    def visit(self, infi: typing.Callable[[], T_Result], inva: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObInterestFixedVariableType1Code.INFI:
            return infi()
        if self is ObInterestFixedVariableType1Code.INVA:
            return inva()
