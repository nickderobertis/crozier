

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InstallExportRequirementsRequestFormat(enum.StrEnum):
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
        if self is InstallExportRequirementsRequestFormat.HTML:
            return html()
        if self is InstallExportRequirementsRequestFormat.IPYNB:
            return ipynb()
        if self is InstallExportRequirementsRequestFormat.MARKDOWN:
            return markdown()
        if self is InstallExportRequirementsRequestFormat.PDF:
            return pdf()
        if self is InstallExportRequirementsRequestFormat.SCRIPT:
            return script()
