

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TeamMemberInvitationStatus(str, enum.Enum):
    """
    Enumerates the possible invitation statuses the team member can have within a business.
    """

    UNINVITED = "UNINVITED"
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"

    def visit(
        self,
        uninvited: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        accepted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TeamMemberInvitationStatus.UNINVITED:
            return uninvited()
        if self is TeamMemberInvitationStatus.PENDING:
            return pending()
        if self is TeamMemberInvitationStatus.ACCEPTED:
            return accepted()
