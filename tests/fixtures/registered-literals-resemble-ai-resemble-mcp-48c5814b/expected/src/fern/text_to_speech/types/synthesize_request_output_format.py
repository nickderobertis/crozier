

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SynthesizeRequestOutputFormat(enum.StrEnum):
    """
    Audio output format
    """

    WAV = "wav"
    MP3 = "mp3"

    def visit(self, wav: typing.Callable[[], T_Result], mp3: typing.Callable[[], T_Result]) -> T_Result:
        if self is SynthesizeRequestOutputFormat.WAV:
            return wav()
        if self is SynthesizeRequestOutputFormat.MP3:
            return mp3()
