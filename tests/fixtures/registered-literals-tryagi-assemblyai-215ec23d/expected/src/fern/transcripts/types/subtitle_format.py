

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SubtitleFormat(enum.StrEnum):
    """
    Format of the subtitles
    """

    SRT = "srt"
    VTT = "vtt"

    def visit(self, srt: typing.Callable[[], T_Result], vtt: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubtitleFormat.SRT:
            return srt()
        if self is SubtitleFormat.VTT:
            return vtt()
