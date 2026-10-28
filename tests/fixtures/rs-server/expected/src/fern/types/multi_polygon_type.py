

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MultiPolygonType(enum.StrEnum):
    MULTI_POLYGON = "MultiPolygon"

    def visit(self, multi_polygon: typing.Callable[[], T_Result]) -> T_Result:
        if self is MultiPolygonType.MULTI_POLYGON:
            return multi_polygon()
