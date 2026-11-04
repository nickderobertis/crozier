

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionAudioParamFormat(enum.StrEnum):
    WAV = "wav"
    AAC = "aac"
    MP3 = "mp3"
    FLAC = "flac"
    OPUS = "opus"
    PCM16 = "pcm16"

    def visit(
        self,
        wav: typing.Callable[[], T_Result],
        aac: typing.Callable[[], T_Result],
        mp3: typing.Callable[[], T_Result],
        flac: typing.Callable[[], T_Result],
        opus: typing.Callable[[], T_Result],
        pcm16: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatCompletionAudioParamFormat.WAV:
            return wav()
        if self is ChatCompletionAudioParamFormat.AAC:
            return aac()
        if self is ChatCompletionAudioParamFormat.MP3:
            return mp3()
        if self is ChatCompletionAudioParamFormat.FLAC:
            return flac()
        if self is ChatCompletionAudioParamFormat.OPUS:
            return opus()
        if self is ChatCompletionAudioParamFormat.PCM16:
            return pcm16()
