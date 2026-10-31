

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AudioFormat(enum.StrEnum):
    MP3 = "mp3"
    WAV = "wav"
    OGG = "ogg"
    ACC = "acc"
    FLAC = "flac"
    RAW = "raw"

    def visit(
        self,
        mp3: typing.Callable[[], T_Result],
        wav: typing.Callable[[], T_Result],
        ogg: typing.Callable[[], T_Result],
        acc: typing.Callable[[], T_Result],
        flac: typing.Callable[[], T_Result],
        raw: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AudioFormat.MP3:
            return mp3()
        if self is AudioFormat.WAV:
            return wav()
        if self is AudioFormat.OGG:
            return ogg()
        if self is AudioFormat.ACC:
            return acc()
        if self is AudioFormat.FLAC:
            return flac()
        if self is AudioFormat.RAW:
            return raw()
