

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExportAsPdfRequestPreset(enum.StrEnum):
    DOCUMENT = "document"
    SLIDES = "slides"

    def visit(self, document: typing.Callable[[], T_Result], slides: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExportAsPdfRequestPreset.DOCUMENT:
            return document()
        if self is ExportAsPdfRequestPreset.SLIDES:
            return slides()
