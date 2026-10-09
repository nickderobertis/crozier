

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SubtitleTrackFormat(enum.StrEnum):
    SRT = "srt"
    VTT = "vtt"
    ASS = "ass"
    UNKNOWN = "unknown"

    def visit(
        self,
        srt: typing.Callable[[], T_Result],
        vtt: typing.Callable[[], T_Result],
        ass: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SubtitleTrackFormat.SRT:
            return srt()
        if self is SubtitleTrackFormat.VTT:
            return vtt()
        if self is SubtitleTrackFormat.ASS:
            return ass()
        if self is SubtitleTrackFormat.UNKNOWN:
            return unknown()
