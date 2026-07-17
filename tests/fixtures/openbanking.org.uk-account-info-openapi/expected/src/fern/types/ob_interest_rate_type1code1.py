

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObInterestRateType1Code1(enum.StrEnum):
    """
    Rate type for Fee/Charge (where it is charged in terms of a rate rather than an amount)
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
        if self is ObInterestRateType1Code1.INBB:
            return inbb()
        if self is ObInterestRateType1Code1.INFR:
            return infr()
        if self is ObInterestRateType1Code1.INGR:
            return ingr()
        if self is ObInterestRateType1Code1.INLR:
            return inlr()
        if self is ObInterestRateType1Code1.INNE:
            return inne()
        if self is ObInterestRateType1Code1.INOT:
            return inot()
