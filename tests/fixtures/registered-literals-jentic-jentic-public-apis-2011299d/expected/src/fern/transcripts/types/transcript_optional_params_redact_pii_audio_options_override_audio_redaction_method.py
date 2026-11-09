

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TranscriptOptionalParamsRedactPiiAudioOptionsOverrideAudioRedactionMethod(enum.StrEnum):
    """
    Specify the method used to redact audio. By default, redacted audio uses a beep sound. Set to `silence` to replace PII with silence instead of a beep.
    """

    SILENCE = "silence"

    def visit(self, silence: typing.Callable[[], T_Result]) -> T_Result:
        if self is TranscriptOptionalParamsRedactPiiAudioOptionsOverrideAudioRedactionMethod.SILENCE:
            return silence()
