

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CancelScheduledPlayResponseMessage(enum.StrEnum):
    """
    Response message
    """

    SCHEDULED_PLAY_CANCELATION_EXECUTED = "Scheduled Play Cancelation Executed"
    SCHED_PLAY_ID_PARAMETER_MUST_BE_PRESENT = "SchedPlayId Parameter must be present"
    SCHEDULED_PLAY_CANCELATION_FAILED_ID_NOT_FOUND = "Scheduled Play Cancelation Failed -- ID not found"
    SCHEDULED_PLAY_CANCELATION_FAILED = "Scheduled Play Cancelation Failed"

    def visit(
        self,
        scheduled_play_cancelation_executed: typing.Callable[[], T_Result],
        sched_play_id_parameter_must_be_present: typing.Callable[[], T_Result],
        scheduled_play_cancelation_failed_id_not_found: typing.Callable[[], T_Result],
        scheduled_play_cancelation_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CancelScheduledPlayResponseMessage.SCHEDULED_PLAY_CANCELATION_EXECUTED:
            return scheduled_play_cancelation_executed()
        if self is CancelScheduledPlayResponseMessage.SCHED_PLAY_ID_PARAMETER_MUST_BE_PRESENT:
            return sched_play_id_parameter_must_be_present()
        if self is CancelScheduledPlayResponseMessage.SCHEDULED_PLAY_CANCELATION_FAILED_ID_NOT_FOUND:
            return scheduled_play_cancelation_failed_id_not_found()
        if self is CancelScheduledPlayResponseMessage.SCHEDULED_PLAY_CANCELATION_FAILED:
            return scheduled_play_cancelation_failed()
