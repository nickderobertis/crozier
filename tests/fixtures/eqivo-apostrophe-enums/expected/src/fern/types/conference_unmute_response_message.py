

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConferenceUnmuteResponseMessage(enum.StrEnum):
    """
    Response message
    """

    CONFERENCE_UNMUTE_EXECUTED = "Conference Unmute Executed"
    CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT = "ConferenceName Parameter must be present"
    MEMBER_ID_PARAMETER_MUST_BE_PRESENT = "MemberID Parameter must be present"
    CONFERENCE_UNMUTE_FAILED_CONFERENCE_NOT_FOUND = "Conference Unmute Failed -- Conference not found"

    def visit(
        self,
        conference_unmute_executed: typing.Callable[[], T_Result],
        conference_name_parameter_must_be_present: typing.Callable[[], T_Result],
        member_id_parameter_must_be_present: typing.Callable[[], T_Result],
        conference_unmute_failed_conference_not_found: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConferenceUnmuteResponseMessage.CONFERENCE_UNMUTE_EXECUTED:
            return conference_unmute_executed()
        if self is ConferenceUnmuteResponseMessage.CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT:
            return conference_name_parameter_must_be_present()
        if self is ConferenceUnmuteResponseMessage.MEMBER_ID_PARAMETER_MUST_BE_PRESENT:
            return member_id_parameter_must_be_present()
        if self is ConferenceUnmuteResponseMessage.CONFERENCE_UNMUTE_FAILED_CONFERENCE_NOT_FOUND:
            return conference_unmute_failed_conference_not_found()
