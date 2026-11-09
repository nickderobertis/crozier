

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConferenceUndeafResponseMessage(enum.StrEnum):
    """
    Response message
    """

    CONFERENCE_UNDEAF_EXECUTED = "Conference Undeaf Executed"
    CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT = "ConferenceName Parameter must be present"
    MEMBER_ID_PARAMETER_MUST_BE_PRESENT = "MemberID Parameter must be present"
    CONFERENCE_UNDEAF_FAILED_CONFERENCE_NOT_FOUND = "Conference Undeaf Failed -- Conference not found"

    def visit(
        self,
        conference_undeaf_executed: typing.Callable[[], T_Result],
        conference_name_parameter_must_be_present: typing.Callable[[], T_Result],
        member_id_parameter_must_be_present: typing.Callable[[], T_Result],
        conference_undeaf_failed_conference_not_found: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConferenceUndeafResponseMessage.CONFERENCE_UNDEAF_EXECUTED:
            return conference_undeaf_executed()
        if self is ConferenceUndeafResponseMessage.CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT:
            return conference_name_parameter_must_be_present()
        if self is ConferenceUndeafResponseMessage.MEMBER_ID_PARAMETER_MUST_BE_PRESENT:
            return member_id_parameter_must_be_present()
        if self is ConferenceUndeafResponseMessage.CONFERENCE_UNDEAF_FAILED_CONFERENCE_NOT_FOUND:
            return conference_undeaf_failed_conference_not_found()
