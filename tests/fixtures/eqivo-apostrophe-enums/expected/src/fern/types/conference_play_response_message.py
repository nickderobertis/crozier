

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConferencePlayResponseMessage(enum.StrEnum):
    """
    Response message
    """

    CONFERENCE_PLAY_EXECUTED = "Conference Play Executed"
    CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT = "ConferenceName Parameter must be present"
    FILE_PATH_PARAMETER_MUST_BE_PRESENT = "FilePath Parameter must be present"
    MEMBER_ID_PARAMETER_MUST_BE_PRESENT = "MemberID Parameter must be present"
    CONFERENCE_PLAY_FAILED_CONFERENCE_NOT_FOUND = "Conference Play Failed -- Conference not found"
    CONFERENCE_PLAY_FAILED = "Conference Play Failed"

    def visit(
        self,
        conference_play_executed: typing.Callable[[], T_Result],
        conference_name_parameter_must_be_present: typing.Callable[[], T_Result],
        file_path_parameter_must_be_present: typing.Callable[[], T_Result],
        member_id_parameter_must_be_present: typing.Callable[[], T_Result],
        conference_play_failed_conference_not_found: typing.Callable[[], T_Result],
        conference_play_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConferencePlayResponseMessage.CONFERENCE_PLAY_EXECUTED:
            return conference_play_executed()
        if self is ConferencePlayResponseMessage.CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT:
            return conference_name_parameter_must_be_present()
        if self is ConferencePlayResponseMessage.FILE_PATH_PARAMETER_MUST_BE_PRESENT:
            return file_path_parameter_must_be_present()
        if self is ConferencePlayResponseMessage.MEMBER_ID_PARAMETER_MUST_BE_PRESENT:
            return member_id_parameter_must_be_present()
        if self is ConferencePlayResponseMessage.CONFERENCE_PLAY_FAILED_CONFERENCE_NOT_FOUND:
            return conference_play_failed_conference_not_found()
        if self is ConferencePlayResponseMessage.CONFERENCE_PLAY_FAILED:
            return conference_play_failed()
