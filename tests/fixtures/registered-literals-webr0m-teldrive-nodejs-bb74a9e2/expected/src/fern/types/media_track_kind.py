

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MediaTrackKind(enum.StrEnum):
    VIDEO = "video"
    AUDIO = "audio"
    SUBTITLE = "subtitle"

    def visit(
        self,
        video: typing.Callable[[], T_Result],
        audio: typing.Callable[[], T_Result],
        subtitle: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MediaTrackKind.VIDEO:
            return video()
        if self is MediaTrackKind.AUDIO:
            return audio()
        if self is MediaTrackKind.SUBTITLE:
            return subtitle()
