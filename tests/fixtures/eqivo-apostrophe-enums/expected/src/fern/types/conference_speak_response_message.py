

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConferenceSpeakResponseMessage(enum.StrEnum):
    """
    Response message
    """

    CONFERENCE_SPEAK_EXECUTED = "Conference Speak Executed"
    CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT = "ConferenceName Parameter must be present"
    TEXT_PARAMETER_MUST_BE_PRESENT = "Text Parameter must be present"
    MEMBER_ID_PARAMETER_MUST_BE_PRESENT = "MemberID Parameter must be present"
    CONFERENCE_SPEAK_FAILED_CONFERENCE_NOT_FOUND = "Conference Speak Failed -- Conference not found"
    CONFERENCE_SPEAK_FAILED = "Conference Speak Failed"

    def visit(
        self,
        conference_speak_executed: typing.Callable[[], T_Result],
        conference_name_parameter_must_be_present: typing.Callable[[], T_Result],
        text_parameter_must_be_present: typing.Callable[[], T_Result],
        member_id_parameter_must_be_present: typing.Callable[[], T_Result],
        conference_speak_failed_conference_not_found: typing.Callable[[], T_Result],
        conference_speak_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConferenceSpeakResponseMessage.CONFERENCE_SPEAK_EXECUTED:
            return conference_speak_executed()
        if self is ConferenceSpeakResponseMessage.CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT:
            return conference_name_parameter_must_be_present()
        if self is ConferenceSpeakResponseMessage.TEXT_PARAMETER_MUST_BE_PRESENT:
            return text_parameter_must_be_present()
        if self is ConferenceSpeakResponseMessage.MEMBER_ID_PARAMETER_MUST_BE_PRESENT:
            return member_id_parameter_must_be_present()
        if self is ConferenceSpeakResponseMessage.CONFERENCE_SPEAK_FAILED_CONFERENCE_NOT_FOUND:
            return conference_speak_failed_conference_not_found()
        if self is ConferenceSpeakResponseMessage.CONFERENCE_SPEAK_FAILED:
            return conference_speak_failed()
