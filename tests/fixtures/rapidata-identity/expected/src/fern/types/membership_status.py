

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MembershipStatus(enum.StrEnum):
    ACTIVE = "Active"
    SUSPENDED = "Suspended"

    def visit(self, active: typing.Callable[[], T_Result], suspended: typing.Callable[[], T_Result]) -> T_Result:
        if self is MembershipStatus.ACTIVE:
            return active()
        if self is MembershipStatus.SUSPENDED:
            return suspended()
