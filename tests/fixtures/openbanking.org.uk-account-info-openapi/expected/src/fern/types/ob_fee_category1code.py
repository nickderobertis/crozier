

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObFeeCategory1Code(str, enum.Enum):
    """
    Categorisation of fees and charges into standard categories.
    """

    FCOT = "FCOT"
    FCRE = "FCRE"
    FCSV = "FCSV"

    def visit(
        self,
        fcot: typing.Callable[[], T_Result],
        fcre: typing.Callable[[], T_Result],
        fcsv: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObFeeCategory1Code.FCOT:
            return fcot()
        if self is ObFeeCategory1Code.FCRE:
            return fcre()
        if self is ObFeeCategory1Code.FCSV:
            return fcsv()
