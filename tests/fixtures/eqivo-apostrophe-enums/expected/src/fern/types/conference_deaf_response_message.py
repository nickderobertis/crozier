

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConferenceDeafResponseMessage(enum.StrEnum):
    """
    Response message
    """

    CONFERENCE_DEAF_EXECUTED = "Conference Deaf Executed"
    CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT = "ConferenceName Parameter must be present"
    MEMBER_ID_PARAMETER_MUST_BE_PRESENT = "MemberID Parameter must be present"
    CONFERENCE_DEAF_FAILED_CONFERENCE_NOT_FOUND = "Conference Deaf Failed -- Conference not found"

    def visit(
        self,
        conference_deaf_executed: typing.Callable[[], T_Result],
        conference_name_parameter_must_be_present: typing.Callable[[], T_Result],
        member_id_parameter_must_be_present: typing.Callable[[], T_Result],
        conference_deaf_failed_conference_not_found: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConferenceDeafResponseMessage.CONFERENCE_DEAF_EXECUTED:
            return conference_deaf_executed()
        if self is ConferenceDeafResponseMessage.CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT:
            return conference_name_parameter_must_be_present()
        if self is ConferenceDeafResponseMessage.MEMBER_ID_PARAMETER_MUST_BE_PRESENT:
            return member_id_parameter_must_be_present()
        if self is ConferenceDeafResponseMessage.CONFERENCE_DEAF_FAILED_CONFERENCE_NOT_FOUND:
            return conference_deaf_failed_conference_not_found()
