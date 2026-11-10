

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSpeechRequestModelOne(enum.StrEnum):
    TTS1 = "tts-1"
    TTS1HD = "tts-1-hd"

    def visit(self, tts1: typing.Callable[[], T_Result], tts1hd: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSpeechRequestModelOne.TTS1:
            return tts1()
        if self is CreateSpeechRequestModelOne.TTS1HD:
            return tts1hd()
