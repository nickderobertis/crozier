

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkBorderStyle(enum.StrEnum):
    SOLID = "solid"
    DASHED = "dashed"
    BEVELED = "beveled"
    INSET = "inset"

    def visit(
        self,
        solid: typing.Callable[[], T_Result],
        dashed: typing.Callable[[], T_Result],
        beveled: typing.Callable[[], T_Result],
        inset: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkBorderStyle.SOLID:
            return solid()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkBorderStyle.DASHED:
            return dashed()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkBorderStyle.BEVELED:
            return beveled()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemInkBorderStyle.INSET:
            return inset()
