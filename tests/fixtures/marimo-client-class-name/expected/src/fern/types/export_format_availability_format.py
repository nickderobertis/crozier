

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExportFormatAvailabilityFormat(enum.StrEnum):
    HTML = "html"
    IPYNB = "ipynb"
    MARKDOWN = "markdown"
    PDF = "pdf"
    SCRIPT = "script"

    def visit(
        self,
        html: typing.Callable[[], T_Result],
        ipynb: typing.Callable[[], T_Result],
        markdown: typing.Callable[[], T_Result],
        pdf: typing.Callable[[], T_Result],
        script: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExportFormatAvailabilityFormat.HTML:
            return html()
        if self is ExportFormatAvailabilityFormat.IPYNB:
            return ipynb()
        if self is ExportFormatAvailabilityFormat.MARKDOWN:
            return markdown()
        if self is ExportFormatAvailabilityFormat.PDF:
            return pdf()
        if self is ExportFormatAvailabilityFormat.SCRIPT:
            return script()
