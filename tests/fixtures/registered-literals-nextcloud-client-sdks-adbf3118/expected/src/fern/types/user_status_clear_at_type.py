

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserStatusClearAtType(enum.StrEnum):
    PERIOD = "period"
    END_OF = "end-of"

    def visit(self, period: typing.Callable[[], T_Result], end_of: typing.Callable[[], T_Result]) -> T_Result:
        if self is UserStatusClearAtType.PERIOD:
            return period()
        if self is UserStatusClearAtType.END_OF:
            return end_of()
