

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SchedulePlayResponseMessage(enum.StrEnum):
    """
    Response message
    """

    PLAY_EXECUTED = "Play Executed"
    CALL_UUID_PARAMETER_MISSING = "CallUUID Parameter Missing"
    SOUNDS_PARAMETER_MISSING = "Sounds Parameter Missing"
    TIME_PARAMETER_MISSING = "Time Parameter Missing"
    TIME_PARAMETER_MUST_BE0 = "Time Parameter must be > 0"
    LEGS_PARAMETER_IS_INVALID = "Legs Parameter is Invalid"
    LENGTH_PARAMETER_MUST_BE_A_POSITIVE_INTEGER = "Length Parameter must be a positive integer"
    SOUNDS_PARAMETER_IS_INVALID = "Sounds Parameter is Invalid"
    PLAY_FAILED_CALL_NOT_FOUND = "Play Failed -- Call not found"
    PLAY_FAILED = "Play Failed"

    def visit(
        self,
        play_executed: typing.Callable[[], T_Result],
        call_uuid_parameter_missing: typing.Callable[[], T_Result],
        sounds_parameter_missing: typing.Callable[[], T_Result],
        time_parameter_missing: typing.Callable[[], T_Result],
        time_parameter_must_be0: typing.Callable[[], T_Result],
        legs_parameter_is_invalid: typing.Callable[[], T_Result],
        length_parameter_must_be_a_positive_integer: typing.Callable[[], T_Result],
        sounds_parameter_is_invalid: typing.Callable[[], T_Result],
        play_failed_call_not_found: typing.Callable[[], T_Result],
        play_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SchedulePlayResponseMessage.PLAY_EXECUTED:
            return play_executed()
        if self is SchedulePlayResponseMessage.CALL_UUID_PARAMETER_MISSING:
            return call_uuid_parameter_missing()
        if self is SchedulePlayResponseMessage.SOUNDS_PARAMETER_MISSING:
            return sounds_parameter_missing()
        if self is SchedulePlayResponseMessage.TIME_PARAMETER_MISSING:
            return time_parameter_missing()
        if self is SchedulePlayResponseMessage.TIME_PARAMETER_MUST_BE0:
            return time_parameter_must_be0()
        if self is SchedulePlayResponseMessage.LEGS_PARAMETER_IS_INVALID:
            return legs_parameter_is_invalid()
        if self is SchedulePlayResponseMessage.LENGTH_PARAMETER_MUST_BE_A_POSITIVE_INTEGER:
            return length_parameter_must_be_a_positive_integer()
        if self is SchedulePlayResponseMessage.SOUNDS_PARAMETER_IS_INVALID:
            return sounds_parameter_is_invalid()
        if self is SchedulePlayResponseMessage.PLAY_FAILED_CALL_NOT_FOUND:
            return play_failed_call_not_found()
        if self is SchedulePlayResponseMessage.PLAY_FAILED:
            return play_failed()
