

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SuperFundType(enum.StrEnum):
    REGULATED = "REGULATED"
    SMSF = "SMSF"

    def visit(self, regulated: typing.Callable[[], T_Result], smsf: typing.Callable[[], T_Result]) -> T_Result:
        if self is SuperFundType.REGULATED:
            return regulated()
        if self is SuperFundType.SMSF:
            return smsf()
