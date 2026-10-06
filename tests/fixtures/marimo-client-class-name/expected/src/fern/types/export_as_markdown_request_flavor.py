

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExportAsMarkdownRequestFlavor(enum.StrEnum):
    MDX = "mdx"
    MYSTMD = "mystmd"
    PYMDOWN = "pymdown"
    QMD = "qmd"

    def visit(
        self,
        mdx: typing.Callable[[], T_Result],
        mystmd: typing.Callable[[], T_Result],
        pymdown: typing.Callable[[], T_Result],
        qmd: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExportAsMarkdownRequestFlavor.MDX:
            return mdx()
        if self is ExportAsMarkdownRequestFlavor.MYSTMD:
            return mystmd()
        if self is ExportAsMarkdownRequestFlavor.PYMDOWN:
            return pymdown()
        if self is ExportAsMarkdownRequestFlavor.QMD:
            return qmd()
