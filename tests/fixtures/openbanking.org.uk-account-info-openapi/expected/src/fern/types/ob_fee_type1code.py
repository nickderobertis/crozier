

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObFeeType1Code(enum.StrEnum):
    """
    Fee/Charge Type
    """

    FEPF = "FEPF"
    FTOT = "FTOT"
    FYAF = "FYAF"
    FYAM = "FYAM"
    FYAQ = "FYAQ"
    FYCP = "FYCP"
    FYDB = "FYDB"
    FYMI = "FYMI"
    FYXX = "FYXX"

    def visit(
        self,
        fepf: typing.Callable[[], T_Result],
        ftot: typing.Callable[[], T_Result],
        fyaf: typing.Callable[[], T_Result],
        fyam: typing.Callable[[], T_Result],
        fyaq: typing.Callable[[], T_Result],
        fycp: typing.Callable[[], T_Result],
        fydb: typing.Callable[[], T_Result],
        fymi: typing.Callable[[], T_Result],
        fyxx: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObFeeType1Code.FEPF:
            return fepf()
        if self is ObFeeType1Code.FTOT:
            return ftot()
        if self is ObFeeType1Code.FYAF:
            return fyaf()
        if self is ObFeeType1Code.FYAM:
            return fyam()
        if self is ObFeeType1Code.FYAQ:
            return fyaq()
        if self is ObFeeType1Code.FYCP:
            return fycp()
        if self is ObFeeType1Code.FYDB:
            return fydb()
        if self is ObFeeType1Code.FYMI:
            return fymi()
        if self is ObFeeType1Code.FYXX:
            return fyxx()
