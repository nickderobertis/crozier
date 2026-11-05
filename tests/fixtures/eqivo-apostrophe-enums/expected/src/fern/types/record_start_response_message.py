

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RecordStartResponseMessage(enum.StrEnum):
    """
    Response message
    """

    RECORD_START_EXECUTED = "RecordStart Executed"
    CALL_UUID_PARAMETER_MUST_BE_PRESENT = "CallUUID Parameter must be present"
    FILE_FORMAT_PARAMETER_MUST_BE = "FileFormat Parameter must be"
    RECORD_START_FAILED_INVALID_TIME_LIMIT = "RecordStart Failed: invalid TimeLimit"
    RECORD_START_FAILED_CALL_NOT_FOUND = "RecordStart Failed -- Call not found"
    RECORD_START_FAILED = "RecordStart Failed"

    def visit(
        self,
        record_start_executed: typing.Callable[[], T_Result],
        call_uuid_parameter_must_be_present: typing.Callable[[], T_Result],
        file_format_parameter_must_be: typing.Callable[[], T_Result],
        record_start_failed_invalid_time_limit: typing.Callable[[], T_Result],
        record_start_failed_call_not_found: typing.Callable[[], T_Result],
        record_start_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RecordStartResponseMessage.RECORD_START_EXECUTED:
            return record_start_executed()
        if self is RecordStartResponseMessage.CALL_UUID_PARAMETER_MUST_BE_PRESENT:
            return call_uuid_parameter_must_be_present()
        if self is RecordStartResponseMessage.FILE_FORMAT_PARAMETER_MUST_BE:
            return file_format_parameter_must_be()
        if self is RecordStartResponseMessage.RECORD_START_FAILED_INVALID_TIME_LIMIT:
            return record_start_failed_invalid_time_limit()
        if self is RecordStartResponseMessage.RECORD_START_FAILED_CALL_NOT_FOUND:
            return record_start_failed_call_not_found()
        if self is RecordStartResponseMessage.RECORD_START_FAILED:
            return record_start_failed()
