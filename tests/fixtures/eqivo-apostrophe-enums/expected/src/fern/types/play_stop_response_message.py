

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlayStopResponseMessage(enum.StrEnum):
    """
    Response message
    """

    PLAY_STOP_EXECUTED = "PlayStop Executed"
    CALL_UUID_PARAMETER_MISSING = "CallUUID Parameter Missing"
    PLAY_STOP_FAILED_CALL_NOT_FOUND = "PlayStop Failed -- Call not found"
    PLAY_STOP_FAILED = "PlayStop Failed"

    def visit(
        self,
        play_stop_executed: typing.Callable[[], T_Result],
        call_uuid_parameter_missing: typing.Callable[[], T_Result],
        play_stop_failed_call_not_found: typing.Callable[[], T_Result],
        play_stop_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlayStopResponseMessage.PLAY_STOP_EXECUTED:
            return play_stop_executed()
        if self is PlayStopResponseMessage.CALL_UUID_PARAMETER_MISSING:
            return call_uuid_parameter_missing()
        if self is PlayStopResponseMessage.PLAY_STOP_FAILED_CALL_NOT_FOUND:
            return play_stop_failed_call_not_found()
        if self is PlayStopResponseMessage.PLAY_STOP_FAILED:
            return play_stop_failed()
