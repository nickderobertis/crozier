

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonBorderStyle(enum.StrEnum):
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
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonBorderStyle.SOLID:
            return solid()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonBorderStyle.DASHED:
            return dashed()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonBorderStyle.BEVELED:
            return beveled()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonBorderStyle.INSET:
            return inset()
