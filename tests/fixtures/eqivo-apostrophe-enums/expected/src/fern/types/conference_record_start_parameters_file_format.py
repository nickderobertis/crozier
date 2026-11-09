

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConferenceRecordStartParametersFileFormat(enum.StrEnum):
    """
    File format (extension)
    """

    WAV = "wav"
    MP3 = "mp3"

    def visit(self, wav: typing.Callable[[], T_Result], mp3: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConferenceRecordStartParametersFileFormat.WAV:
            return wav()
        if self is ConferenceRecordStartParametersFileFormat.MP3:
            return mp3()
