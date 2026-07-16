

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RateType(enum.StrEnum):
    FIXEDAMOUNT = "FIXEDAMOUNT"
    MULTIPLE = "MULTIPLE"
    RATEPERUNIT = "RATEPERUNIT"

    def visit(
        self,
        fixedamount: typing.Callable[[], T_Result],
        multiple: typing.Callable[[], T_Result],
        rateperunit: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RateType.FIXEDAMOUNT:
            return fixedamount()
        if self is RateType.MULTIPLE:
            return multiple()
        if self is RateType.RATEPERUNIT:
            return rateperunit()
