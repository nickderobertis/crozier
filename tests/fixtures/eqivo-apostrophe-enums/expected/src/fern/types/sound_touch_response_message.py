

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SoundTouchResponseMessage(enum.StrEnum):
    """
    Response message
    """

    SOUND_TOUCH_EXECUTED = "SoundTouch Executed"
    CALL_UUID_PARAMETER_MISSING = "CallUUID Parameter Missing"
    AUDIO_DIRECTION_PARAMETER_MUST_BE_IN_OR_OUT = "AudioDirection Parameter Must be 'in' or 'out'"
    PITCH_SEMI_TONES_PARAMETER_MUST_BE_FLOAT = "PitchSemiTones Parameter must be float"
    PITCH_SEMI_TONES_PARAMETER_MUST_BE_BETWEEN14AND14 = "PitchSemiTones Parameter must be between -14 and 14"
    PITCH_OCTAVES_PARAMETER_MUST_BE_FLOAT = "PitchOctaves Parameter must be float"
    PITCH_OCTAVES_PARAMETER_MUST_BE_BETWEEN1AND1 = "PitchOctaves Parameter must be between -1 and 1"
    PITCH_PARAMETER_MUST_BE_FLOAT = "Pitch Parameter must be float"
    PITCH_PARAMETER_MUST_BE0 = "Pitch Parameter must be > 0"
    RATE_PARAMETER_MUST_BE_FLOAT = "Rate Parameter must be float"
    RATE_PARAMETER_MUST_BE0 = "Rate Parameter must be > 0"
    TEMPO_PARAMETER_MUST_BE_FLOAT = "Tempo Parameter must be float"
    TEMPO_PARAMETER_MUST_BE0 = "Tempo Parameter must be > 0"
    SOUND_TOUCH_FAILED_CALL_NOT_FOUND = "SoundTouch Failed -- Call not found"
    SOUND_TOUCH_FAILED = "SoundTouch Failed"

    def visit(
        self,
        sound_touch_executed: typing.Callable[[], T_Result],
        call_uuid_parameter_missing: typing.Callable[[], T_Result],
        audio_direction_parameter_must_be_in_or_out: typing.Callable[[], T_Result],
        pitch_semi_tones_parameter_must_be_float: typing.Callable[[], T_Result],
        pitch_semi_tones_parameter_must_be_between14and14: typing.Callable[[], T_Result],
        pitch_octaves_parameter_must_be_float: typing.Callable[[], T_Result],
        pitch_octaves_parameter_must_be_between1and1: typing.Callable[[], T_Result],
        pitch_parameter_must_be_float: typing.Callable[[], T_Result],
        pitch_parameter_must_be0: typing.Callable[[], T_Result],
        rate_parameter_must_be_float: typing.Callable[[], T_Result],
        rate_parameter_must_be0: typing.Callable[[], T_Result],
        tempo_parameter_must_be_float: typing.Callable[[], T_Result],
        tempo_parameter_must_be0: typing.Callable[[], T_Result],
        sound_touch_failed_call_not_found: typing.Callable[[], T_Result],
        sound_touch_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SoundTouchResponseMessage.SOUND_TOUCH_EXECUTED:
            return sound_touch_executed()
        if self is SoundTouchResponseMessage.CALL_UUID_PARAMETER_MISSING:
            return call_uuid_parameter_missing()
        if self is SoundTouchResponseMessage.AUDIO_DIRECTION_PARAMETER_MUST_BE_IN_OR_OUT:
            return audio_direction_parameter_must_be_in_or_out()
        if self is SoundTouchResponseMessage.PITCH_SEMI_TONES_PARAMETER_MUST_BE_FLOAT:
            return pitch_semi_tones_parameter_must_be_float()
        if self is SoundTouchResponseMessage.PITCH_SEMI_TONES_PARAMETER_MUST_BE_BETWEEN14AND14:
            return pitch_semi_tones_parameter_must_be_between14and14()
        if self is SoundTouchResponseMessage.PITCH_OCTAVES_PARAMETER_MUST_BE_FLOAT:
            return pitch_octaves_parameter_must_be_float()
        if self is SoundTouchResponseMessage.PITCH_OCTAVES_PARAMETER_MUST_BE_BETWEEN1AND1:
            return pitch_octaves_parameter_must_be_between1and1()
        if self is SoundTouchResponseMessage.PITCH_PARAMETER_MUST_BE_FLOAT:
            return pitch_parameter_must_be_float()
        if self is SoundTouchResponseMessage.PITCH_PARAMETER_MUST_BE0:
            return pitch_parameter_must_be0()
        if self is SoundTouchResponseMessage.RATE_PARAMETER_MUST_BE_FLOAT:
            return rate_parameter_must_be_float()
        if self is SoundTouchResponseMessage.RATE_PARAMETER_MUST_BE0:
            return rate_parameter_must_be0()
        if self is SoundTouchResponseMessage.TEMPO_PARAMETER_MUST_BE_FLOAT:
            return tempo_parameter_must_be_float()
        if self is SoundTouchResponseMessage.TEMPO_PARAMETER_MUST_BE0:
            return tempo_parameter_must_be0()
        if self is SoundTouchResponseMessage.SOUND_TOUCH_FAILED_CALL_NOT_FOUND:
            return sound_touch_failed_call_not_found()
        if self is SoundTouchResponseMessage.SOUND_TOUCH_FAILED:
            return sound_touch_failed()
