

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SuperannuationCalculationType(enum.StrEnum):
    FIXEDAMOUNT = "FIXEDAMOUNT"
    PERCENTAGEOFEARNINGS = "PERCENTAGEOFEARNINGS"
    STATUTORY = "STATUTORY"

    def visit(
        self,
        fixedamount: typing.Callable[[], T_Result],
        percentageofearnings: typing.Callable[[], T_Result],
        statutory: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SuperannuationCalculationType.FIXEDAMOUNT:
            return fixedamount()
        if self is SuperannuationCalculationType.PERCENTAGEOFEARNINGS:
            return percentageofearnings()
        if self is SuperannuationCalculationType.STATUTORY:
            return statutory()
