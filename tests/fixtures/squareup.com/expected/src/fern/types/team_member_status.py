

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TeamMemberStatus(enum.StrEnum):
    """
    Enumerates the possible statuses the team member can have within a business.
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is TeamMemberStatus.ACTIVE:
            return active()
        if self is TeamMemberStatus.INACTIVE:
            return inactive()
