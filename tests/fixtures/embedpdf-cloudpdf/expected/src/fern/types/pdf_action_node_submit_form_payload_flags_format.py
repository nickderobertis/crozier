

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PdfActionNodeSubmitFormPayloadFlagsFormat(enum.StrEnum):
    FDF = "fdf"
    HTML = "html"
    XFDF = "xfdf"
    PDF = "pdf"

    def visit(
        self,
        fdf: typing.Callable[[], T_Result],
        html: typing.Callable[[], T_Result],
        xfdf: typing.Callable[[], T_Result],
        pdf: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PdfActionNodeSubmitFormPayloadFlagsFormat.FDF:
            return fdf()
        if self is PdfActionNodeSubmitFormPayloadFlagsFormat.HTML:
            return html()
        if self is PdfActionNodeSubmitFormPayloadFlagsFormat.XFDF:
            return xfdf()
        if self is PdfActionNodeSubmitFormPayloadFlagsFormat.PDF:
            return pdf()
