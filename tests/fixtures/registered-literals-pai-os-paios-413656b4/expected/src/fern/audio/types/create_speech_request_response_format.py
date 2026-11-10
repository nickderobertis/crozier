

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSpeechRequestResponseFormat(enum.StrEnum):
    """
    The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`, `wav`, and `pcm`.
    """

    MP3 = "mp3"
    OPUS = "opus"
    AAC = "aac"
    FLAC = "flac"
    WAV = "wav"
    PCM = "pcm"

    def visit(
        self,
        mp3: typing.Callable[[], T_Result],
        opus: typing.Callable[[], T_Result],
        aac: typing.Callable[[], T_Result],
        flac: typing.Callable[[], T_Result],
        wav: typing.Callable[[], T_Result],
        pcm: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateSpeechRequestResponseFormat.MP3:
            return mp3()
        if self is CreateSpeechRequestResponseFormat.OPUS:
            return opus()
        if self is CreateSpeechRequestResponseFormat.AAC:
            return aac()
        if self is CreateSpeechRequestResponseFormat.FLAC:
            return flac()
        if self is CreateSpeechRequestResponseFormat.WAV:
            return wav()
        if self is CreateSpeechRequestResponseFormat.PCM:
            return pcm()
