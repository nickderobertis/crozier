

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConferenceMuteResponseMessage(enum.StrEnum):
    """
    Response message
    """

    CONFERENCE_MUTE_EXECUTED = "Conference Mute Executed"
    CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT = "ConferenceName Parameter must be present"
    MEMBER_ID_PARAMETER_MUST_BE_PRESENT = "MemberID Parameter must be present"
    CONFERENCE_MUTE_FAILED_CONFERENCE_NOT_FOUND = "Conference Mute Failed -- Conference not found"

    def visit(
        self,
        conference_mute_executed: typing.Callable[[], T_Result],
        conference_name_parameter_must_be_present: typing.Callable[[], T_Result],
        member_id_parameter_must_be_present: typing.Callable[[], T_Result],
        conference_mute_failed_conference_not_found: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConferenceMuteResponseMessage.CONFERENCE_MUTE_EXECUTED:
            return conference_mute_executed()
        if self is ConferenceMuteResponseMessage.CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT:
            return conference_name_parameter_must_be_present()
        if self is ConferenceMuteResponseMessage.MEMBER_ID_PARAMETER_MUST_BE_PRESENT:
            return member_id_parameter_must_be_present()
        if self is ConferenceMuteResponseMessage.CONFERENCE_MUTE_FAILED_CONFERENCE_NOT_FOUND:
            return conference_mute_failed_conference_not_found()
