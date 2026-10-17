

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CaptionFormat(enum.StrEnum):
    TXT = "txt"
    VTT = "vtt"
    SRT = "srt"

    def visit(
        self, txt: typing.Callable[[], T_Result], vtt: typing.Callable[[], T_Result], srt: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is CaptionFormat.TXT:
            return txt()
        if self is CaptionFormat.VTT:
            return vtt()
        if self is CaptionFormat.SRT:
            return srt()
