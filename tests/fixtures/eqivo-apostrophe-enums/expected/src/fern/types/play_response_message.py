

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlayResponseMessage(enum.StrEnum):
    """
    Response message
    """

    PLAY_EXECUTED = "Play Executed"
    CALL_UUID_PARAMETER_MISSING = "CallUUID Parameter Missing"
    SOUNDS_PARAMETER_MISSING = "Sounds Parameter Missing"
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
        legs_parameter_is_invalid: typing.Callable[[], T_Result],
        length_parameter_must_be_a_positive_integer: typing.Callable[[], T_Result],
        sounds_parameter_is_invalid: typing.Callable[[], T_Result],
        play_failed_call_not_found: typing.Callable[[], T_Result],
        play_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlayResponseMessage.PLAY_EXECUTED:
            return play_executed()
        if self is PlayResponseMessage.CALL_UUID_PARAMETER_MISSING:
            return call_uuid_parameter_missing()
        if self is PlayResponseMessage.SOUNDS_PARAMETER_MISSING:
            return sounds_parameter_missing()
        if self is PlayResponseMessage.LEGS_PARAMETER_IS_INVALID:
            return legs_parameter_is_invalid()
        if self is PlayResponseMessage.LENGTH_PARAMETER_MUST_BE_A_POSITIVE_INTEGER:
            return length_parameter_must_be_a_positive_integer()
        if self is PlayResponseMessage.SOUNDS_PARAMETER_IS_INVALID:
            return sounds_parameter_is_invalid()
        if self is PlayResponseMessage.PLAY_FAILED_CALL_NOT_FOUND:
            return play_failed_call_not_found()
        if self is PlayResponseMessage.PLAY_FAILED:
            return play_failed()
