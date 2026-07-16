

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class SuperFundType(str, enum.Enum):
    REGULATED = "REGULATED"
    SMSF = "SMSF"

    def visit(self, regulated: typing.Callable[[], T_Result], smsf: typing.Callable[[], T_Result]) -> T_Result:
        if self is SuperFundType.REGULATED:
            return regulated()
        if self is SuperFundType.SMSF:
            return smsf()
