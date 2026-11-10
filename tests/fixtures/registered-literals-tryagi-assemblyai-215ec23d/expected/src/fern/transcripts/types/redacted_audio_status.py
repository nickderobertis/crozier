

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RedactedAudioStatus(enum.StrEnum):
    """
    The status of the redacted audio
    """

    REDACTED_AUDIO_READY = "redacted_audio_ready"

    def visit(self, redacted_audio_ready: typing.Callable[[], T_Result]) -> T_Result:
        if self is RedactedAudioStatus.REDACTED_AUDIO_READY:
            return redacted_audio_ready()
