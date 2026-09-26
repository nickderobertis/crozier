

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class ExportDataFormsRequestFormat(enum.StrEnum):
    FDF = "fdf"
    XFDF = "xfdf"

    def visit(self, fdf: typing.Callable[[], T_Result], xfdf: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExportDataFormsRequestFormat.FDF:
            return fdf()
        if self is ExportDataFormsRequestFormat.XFDF:
            return xfdf()
