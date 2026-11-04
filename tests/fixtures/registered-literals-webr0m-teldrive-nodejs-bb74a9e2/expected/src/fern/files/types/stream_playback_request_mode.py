

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class StreamPlaybackRequestMode(enum.StrEnum):
    ORIGINAL = "original"
    AUDIO = "audio"
    VIDEO = "video"

    def visit(
        self,
        original: typing.Callable[[], T_Result],
        audio: typing.Callable[[], T_Result],
        video: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StreamPlaybackRequestMode.ORIGINAL:
            return original()
        if self is StreamPlaybackRequestMode.AUDIO:
            return audio()
        if self is StreamPlaybackRequestMode.VIDEO:
            return video()
