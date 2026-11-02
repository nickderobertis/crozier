

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LeaveRole(enum.StrEnum):
    ANNUAL = "annual"
    SICK = "sick"

    def visit(self, annual: typing.Callable[[], T_Result], sick: typing.Callable[[], T_Result]) -> T_Result:
        if self is LeaveRole.ANNUAL:
            return annual()
        if self is LeaveRole.SICK:
            return sick()
