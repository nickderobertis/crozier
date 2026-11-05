

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SoundTouchStopResponseMessage(enum.StrEnum):
    """
    Response message
    """

    SOUND_TOUCH_STOP_EXECUTED = "SoundTouchStop Executed"
    CALL_UUID_PARAMETER_MISSING = "CallUUID Parameter Missing"
    SOUND_TOUCH_STOP_FAILED_CALL_NOT_FOUND = "SoundTouchStop Failed -- Call not found"
    SOUND_TOUCH_STOP_FAILED = "SoundTouchStop Failed"

    def visit(
        self,
        sound_touch_stop_executed: typing.Callable[[], T_Result],
        call_uuid_parameter_missing: typing.Callable[[], T_Result],
        sound_touch_stop_failed_call_not_found: typing.Callable[[], T_Result],
        sound_touch_stop_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SoundTouchStopResponseMessage.SOUND_TOUCH_STOP_EXECUTED:
            return sound_touch_stop_executed()
        if self is SoundTouchStopResponseMessage.CALL_UUID_PARAMETER_MISSING:
            return call_uuid_parameter_missing()
        if self is SoundTouchStopResponseMessage.SOUND_TOUCH_STOP_FAILED_CALL_NOT_FOUND:
            return sound_touch_stop_failed_call_not_found()
        if self is SoundTouchStopResponseMessage.SOUND_TOUCH_STOP_FAILED:
            return sound_touch_stop_failed()
