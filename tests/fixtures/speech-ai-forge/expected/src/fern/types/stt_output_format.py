

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SttOutputFormat(enum.StrEnum):
    TXT = "txt"
    VTT = "vtt"
    SRT = "srt"
    TSV = "tsv"
    LRC = "lrc"
    JSON = "json"

    def visit(
        self,
        txt: typing.Callable[[], T_Result],
        vtt: typing.Callable[[], T_Result],
        srt: typing.Callable[[], T_Result],
        tsv: typing.Callable[[], T_Result],
        lrc: typing.Callable[[], T_Result],
        json: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SttOutputFormat.TXT:
            return txt()
        if self is SttOutputFormat.VTT:
            return vtt()
        if self is SttOutputFormat.SRT:
            return srt()
        if self is SttOutputFormat.TSV:
            return tsv()
        if self is SttOutputFormat.LRC:
            return lrc()
        if self is SttOutputFormat.JSON:
            return json()
