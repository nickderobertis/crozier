

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConferenceKickResponseMessage(enum.StrEnum):
    """
    Response message
    """

    CONFERENCE_KICK_EXECUTED = "Conference Kick Executed"
    CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT = "ConferenceName Parameter must be present"
    MEMBER_ID_PARAMETER_MUST_BE_PRESENT = "MemberID Parameter must be present"
    CONFERENCE_KICK_FAILED_CONFERENCE_NOT_FOUND = "Conference Kick Failed -- Conference not found"

    def visit(
        self,
        conference_kick_executed: typing.Callable[[], T_Result],
        conference_name_parameter_must_be_present: typing.Callable[[], T_Result],
        member_id_parameter_must_be_present: typing.Callable[[], T_Result],
        conference_kick_failed_conference_not_found: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConferenceKickResponseMessage.CONFERENCE_KICK_EXECUTED:
            return conference_kick_executed()
        if self is ConferenceKickResponseMessage.CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT:
            return conference_name_parameter_must_be_present()
        if self is ConferenceKickResponseMessage.MEMBER_ID_PARAMETER_MUST_BE_PRESENT:
            return member_id_parameter_must_be_present()
        if self is ConferenceKickResponseMessage.CONFERENCE_KICK_FAILED_CONFERENCE_NOT_FOUND:
            return conference_kick_failed_conference_not_found()
