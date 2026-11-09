

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CancelScheduledHangupResponseMessage(enum.StrEnum):
    """
    Response message
    """

    SCHEDULED_HANGUP_CANCELATION_EXECUTED = "Scheduled Hangup Cancelation Executed"
    SCHED_HANGUP_ID_PARAMETER_MUST_BE_PRESENT = "SchedHangupId Parameter must be present"
    SCHEDULED_HANGUP_CANCELATION_FAILED_ID_NOT_FOUND = "Scheduled Hangup Cancelation Failed -- ID not found"
    SCHEDULED_HANGUP_CANCELATION_FAILED = "Scheduled Hangup Cancelation Failed"

    def visit(
        self,
        scheduled_hangup_cancelation_executed: typing.Callable[[], T_Result],
        sched_hangup_id_parameter_must_be_present: typing.Callable[[], T_Result],
        scheduled_hangup_cancelation_failed_id_not_found: typing.Callable[[], T_Result],
        scheduled_hangup_cancelation_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CancelScheduledHangupResponseMessage.SCHEDULED_HANGUP_CANCELATION_EXECUTED:
            return scheduled_hangup_cancelation_executed()
        if self is CancelScheduledHangupResponseMessage.SCHED_HANGUP_ID_PARAMETER_MUST_BE_PRESENT:
            return sched_hangup_id_parameter_must_be_present()
        if self is CancelScheduledHangupResponseMessage.SCHEDULED_HANGUP_CANCELATION_FAILED_ID_NOT_FOUND:
            return scheduled_hangup_cancelation_failed_id_not_found()
        if self is CancelScheduledHangupResponseMessage.SCHEDULED_HANGUP_CANCELATION_FAILED:
            return scheduled_hangup_cancelation_failed()
