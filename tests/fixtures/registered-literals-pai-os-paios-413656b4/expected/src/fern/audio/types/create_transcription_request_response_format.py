

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateTranscriptionRequestResponseFormat(enum.StrEnum):
    """
    The format of the transcript output, in one of these options: `json`, `text`, `srt`, `verbose_json`, or `vtt`.
    """

    JSON = "json"
    TEXT = "text"
    SRT = "srt"
    VERBOSE_JSON = "verbose_json"
    VTT = "vtt"

    def visit(
        self,
        json: typing.Callable[[], T_Result],
        text: typing.Callable[[], T_Result],
        srt: typing.Callable[[], T_Result],
        verbose_json: typing.Callable[[], T_Result],
        vtt: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateTranscriptionRequestResponseFormat.JSON:
            return json()
        if self is CreateTranscriptionRequestResponseFormat.TEXT:
            return text()
        if self is CreateTranscriptionRequestResponseFormat.SRT:
            return srt()
        if self is CreateTranscriptionRequestResponseFormat.VERBOSE_JSON:
            return verbose_json()
        if self is CreateTranscriptionRequestResponseFormat.VTT:
            return vtt()
