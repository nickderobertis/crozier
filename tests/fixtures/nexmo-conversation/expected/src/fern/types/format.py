

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Format(enum.StrEnum):
    """
    Record the Conversation in a specific format.
    """

    MP3 = "mp3"
    WAV = "wav"

    def visit(self, mp3: typing.Callable[[], T_Result], wav: typing.Callable[[], T_Result]) -> T_Result:
        if self is Format.MP3:
            return mp3()
        if self is Format.WAV:
            return wav()
