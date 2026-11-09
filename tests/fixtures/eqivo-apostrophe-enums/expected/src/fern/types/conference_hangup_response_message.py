

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConferenceHangupResponseMessage(enum.StrEnum):
    """
    Response message
    """

    CONFERENCE_HANGUP_EXECUTED = "Conference Hangup Executed"
    CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT = "ConferenceName Parameter must be present"
    MEMBER_ID_PARAMETER_MUST_BE_PRESENT = "MemberID Parameter must be present"
    CONFERENCE_HANGUP_FAILED_CONFERENCE_NOT_FOUND = "Conference Hangup Failed -- Conference not found"

    def visit(
        self,
        conference_hangup_executed: typing.Callable[[], T_Result],
        conference_name_parameter_must_be_present: typing.Callable[[], T_Result],
        member_id_parameter_must_be_present: typing.Callable[[], T_Result],
        conference_hangup_failed_conference_not_found: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConferenceHangupResponseMessage.CONFERENCE_HANGUP_EXECUTED:
            return conference_hangup_executed()
        if self is ConferenceHangupResponseMessage.CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT:
            return conference_name_parameter_must_be_present()
        if self is ConferenceHangupResponseMessage.MEMBER_ID_PARAMETER_MUST_BE_PRESENT:
            return member_id_parameter_must_be_present()
        if self is ConferenceHangupResponseMessage.CONFERENCE_HANGUP_FAILED_CONFERENCE_NOT_FOUND:
            return conference_hangup_failed_conference_not_found()
