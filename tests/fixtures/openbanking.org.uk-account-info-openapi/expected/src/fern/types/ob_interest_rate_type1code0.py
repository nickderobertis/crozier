

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObInterestRateType1Code0(enum.StrEnum):
    """
    Rate type for overdraft fee/charge (where it is charged in terms of a rate rather than an amount)
    """

    INBB = "INBB"
    INFR = "INFR"
    INGR = "INGR"
    INLR = "INLR"
    INNE = "INNE"
    INOT = "INOT"

    def visit(
        self,
        inbb: typing.Callable[[], T_Result],
        infr: typing.Callable[[], T_Result],
        ingr: typing.Callable[[], T_Result],
        inlr: typing.Callable[[], T_Result],
        inne: typing.Callable[[], T_Result],
        inot: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObInterestRateType1Code0.INBB:
            return inbb()
        if self is ObInterestRateType1Code0.INFR:
            return infr()
        if self is ObInterestRateType1Code0.INGR:
            return ingr()
        if self is ObInterestRateType1Code0.INLR:
            return inlr()
        if self is ObInterestRateType1Code0.INNE:
            return inne()
        if self is ObInterestRateType1Code0.INOT:
            return inot()
