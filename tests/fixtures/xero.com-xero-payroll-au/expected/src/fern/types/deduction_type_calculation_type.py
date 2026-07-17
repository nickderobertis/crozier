

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeductionTypeCalculationType(enum.StrEnum):
    FIXEDAMOUNT = "FIXEDAMOUNT"
    PRETAX = "PRETAX"
    POSTTAX = "POSTTAX"

    def visit(
        self,
        fixedamount: typing.Callable[[], T_Result],
        pretax: typing.Callable[[], T_Result],
        posttax: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeductionTypeCalculationType.FIXEDAMOUNT:
            return fixedamount()
        if self is DeductionTypeCalculationType.PRETAX:
            return pretax()
        if self is DeductionTypeCalculationType.POSTTAX:
            return posttax()
