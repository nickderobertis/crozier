

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObInterestCalculationMethod1Code(str, enum.Enum):
    """
    Methods of calculating interest
    """

    ITCO = "ITCO"
    ITOT = "ITOT"
    ITSI = "ITSI"

    def visit(
        self,
        itco: typing.Callable[[], T_Result],
        itot: typing.Callable[[], T_Result],
        itsi: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObInterestCalculationMethod1Code.ITCO:
            return itco()
        if self is ObInterestCalculationMethod1Code.ITOT:
            return itot()
        if self is ObInterestCalculationMethod1Code.ITSI:
            return itsi()
