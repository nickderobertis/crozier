

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduleHangupResponseMessage(enum.StrEnum):
    """
    Response message
    """

    SCHEDULE_HANGUP_EXECUTED = "ScheduleHangup Executed"
    CALL_UUID_PARAMETER_MUST_BE_PRESENT = "CallUUID Parameter must be present"
    TIME_PARAMETER_MUST_BE_PRESENT = "Time Parameter must be present"
    TIME_PARAMETER_MUST_BE0 = "Time Parameter must be > 0!"
    SCHEDULE_HANGUP_FAILED_CALL_NOT_FOUND = "ScheduleHangup Failed -- Call not found"
    SCHEDULE_HANGUP_FAILED = "ScheduleHangup Failed"

    def visit(
        self,
        schedule_hangup_executed: typing.Callable[[], T_Result],
        call_uuid_parameter_must_be_present: typing.Callable[[], T_Result],
        time_parameter_must_be_present: typing.Callable[[], T_Result],
        time_parameter_must_be0: typing.Callable[[], T_Result],
        schedule_hangup_failed_call_not_found: typing.Callable[[], T_Result],
        schedule_hangup_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ScheduleHangupResponseMessage.SCHEDULE_HANGUP_EXECUTED:
            return schedule_hangup_executed()
        if self is ScheduleHangupResponseMessage.CALL_UUID_PARAMETER_MUST_BE_PRESENT:
            return call_uuid_parameter_must_be_present()
        if self is ScheduleHangupResponseMessage.TIME_PARAMETER_MUST_BE_PRESENT:
            return time_parameter_must_be_present()
        if self is ScheduleHangupResponseMessage.TIME_PARAMETER_MUST_BE0:
            return time_parameter_must_be0()
        if self is ScheduleHangupResponseMessage.SCHEDULE_HANGUP_FAILED_CALL_NOT_FOUND:
            return schedule_hangup_failed_call_not_found()
        if self is ScheduleHangupResponseMessage.SCHEDULE_HANGUP_FAILED:
            return schedule_hangup_failed()
