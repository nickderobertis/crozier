

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TeamMembershipCollaboratorType(enum.StrEnum):
    TEAM_MEMBERSHIP = "TEAM_MEMBERSHIP"

    def visit(self, team_membership: typing.Callable[[], T_Result]) -> T_Result:
        if self is TeamMembershipCollaboratorType.TEAM_MEMBERSHIP:
            return team_membership()
