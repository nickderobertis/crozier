

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConferenceRecordStartResponseMessage(enum.StrEnum):
    """
    Response message
    """

    CONFERENCE_RECORD_START_EXECUTED = "Conference RecordStart Executed"
    CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT = "ConferenceName Parameter must be present"
    FILE_FORMAT_PARAMETER_MUST_BE = "FileFormat Parameter must be"
    CONFERENCE_RECORD_START_FAILED = "Conference RecordStart Failed"
    CONFERENCE_RECORD_START_FAILED_CONFERENCE_NOT_FOUND = "Conference RecordStart Failed -- Conference not found"

    def visit(
        self,
        conference_record_start_executed: typing.Callable[[], T_Result],
        conference_name_parameter_must_be_present: typing.Callable[[], T_Result],
        file_format_parameter_must_be: typing.Callable[[], T_Result],
        conference_record_start_failed: typing.Callable[[], T_Result],
        conference_record_start_failed_conference_not_found: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConferenceRecordStartResponseMessage.CONFERENCE_RECORD_START_EXECUTED:
            return conference_record_start_executed()
        if self is ConferenceRecordStartResponseMessage.CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT:
            return conference_name_parameter_must_be_present()
        if self is ConferenceRecordStartResponseMessage.FILE_FORMAT_PARAMETER_MUST_BE:
            return file_format_parameter_must_be()
        if self is ConferenceRecordStartResponseMessage.CONFERENCE_RECORD_START_FAILED:
            return conference_record_start_failed()
        if self is ConferenceRecordStartResponseMessage.CONFERENCE_RECORD_START_FAILED_CONFERENCE_NOT_FOUND:
            return conference_record_start_failed_conference_not_found()
