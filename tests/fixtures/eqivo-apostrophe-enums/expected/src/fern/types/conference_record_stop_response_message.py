

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConferenceRecordStopResponseMessage(enum.StrEnum):
    """
    Response message
    """

    CONFERENCE_RECORD_STOP_EXECUTED = "Conference RecordStop Executed"
    CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT = "ConferenceName Parameter must be present"
    RECORD_FILE_PARAMETER_MUST_BE_PRESENT = "RecordFile Parameter must be present"
    CONFERENCE_RECORD_STOP_FAILED = "Conference RecordStop Failed"
    CONFERENCE_RECORD_STOP_FAILED_CONFERENCE_NOT_FOUND = "Conference RecordStop Failed -- Conference not found"

    def visit(
        self,
        conference_record_stop_executed: typing.Callable[[], T_Result],
        conference_name_parameter_must_be_present: typing.Callable[[], T_Result],
        record_file_parameter_must_be_present: typing.Callable[[], T_Result],
        conference_record_stop_failed: typing.Callable[[], T_Result],
        conference_record_stop_failed_conference_not_found: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConferenceRecordStopResponseMessage.CONFERENCE_RECORD_STOP_EXECUTED:
            return conference_record_stop_executed()
        if self is ConferenceRecordStopResponseMessage.CONFERENCE_NAME_PARAMETER_MUST_BE_PRESENT:
            return conference_name_parameter_must_be_present()
        if self is ConferenceRecordStopResponseMessage.RECORD_FILE_PARAMETER_MUST_BE_PRESENT:
            return record_file_parameter_must_be_present()
        if self is ConferenceRecordStopResponseMessage.CONFERENCE_RECORD_STOP_FAILED:
            return conference_record_stop_failed()
        if self is ConferenceRecordStopResponseMessage.CONFERENCE_RECORD_STOP_FAILED_CONFERENCE_NOT_FOUND:
            return conference_record_stop_failed_conference_not_found()
