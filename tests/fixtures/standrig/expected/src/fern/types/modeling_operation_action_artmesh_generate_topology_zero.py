

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionArtmeshGenerateTopologyZero(enum.StrEnum):
    RECT_GRID = "rect-grid"

    def visit(self, rect_grid: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionArtmeshGenerateTopologyZero.RECT_GRID:
            return rect_grid()
