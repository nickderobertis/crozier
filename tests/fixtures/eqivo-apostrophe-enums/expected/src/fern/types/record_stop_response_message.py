

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RecordStopResponseMessage(enum.StrEnum):
    """
    Response message
    """

    RECORD_STOP_EXECUTED = "RecordStop Executed"
    CALL_UUID_PARAMETER_MUST_BE_PRESENT = "CallUUID Parameter must be present"
    RECORD_FILE_PARAMETER_MUST_BE_PRESENT = "RecordFile Parameter must be present"
    RECORD_STOP_FAILED_CALL_NOT_FOUND = "RecordStop Failed -- Call not found"
    RECORD_STOP_FAILED = "RecordStop Failed"

    def visit(
        self,
        record_stop_executed: typing.Callable[[], T_Result],
        call_uuid_parameter_must_be_present: typing.Callable[[], T_Result],
        record_file_parameter_must_be_present: typing.Callable[[], T_Result],
        record_stop_failed_call_not_found: typing.Callable[[], T_Result],
        record_stop_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RecordStopResponseMessage.RECORD_STOP_EXECUTED:
            return record_stop_executed()
        if self is RecordStopResponseMessage.CALL_UUID_PARAMETER_MUST_BE_PRESENT:
            return call_uuid_parameter_must_be_present()
        if self is RecordStopResponseMessage.RECORD_FILE_PARAMETER_MUST_BE_PRESENT:
            return record_file_parameter_must_be_present()
        if self is RecordStopResponseMessage.RECORD_STOP_FAILED_CALL_NOT_FOUND:
            return record_stop_failed_call_not_found()
        if self is RecordStopResponseMessage.RECORD_STOP_FAILED:
            return record_stop_failed()
