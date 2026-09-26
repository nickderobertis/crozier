

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AllowedFilesAudioItem(enum.StrEnum):
    ALL = "*"
    MP3 = ".mp3"
    WAV = ".wav"
    M4A = ".m4a"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        mp3: typing.Callable[[], T_Result],
        wav: typing.Callable[[], T_Result],
        m4a: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AllowedFilesAudioItem.ALL:
            return all_()
        if self is AllowedFilesAudioItem.MP3:
            return mp3()
        if self is AllowedFilesAudioItem.WAV:
            return wav()
        if self is AllowedFilesAudioItem.M4A:
            return m4a()
