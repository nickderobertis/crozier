

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SimpleDataModelsGeometryCollectionGeometriesItemType(enum.StrEnum):
    MULTI_POLYGON = "MultiPolygon"

    def visit(self, multi_polygon: typing.Callable[[], T_Result]) -> T_Result:
        if self is SimpleDataModelsGeometryCollectionGeometriesItemType.MULTI_POLYGON:
            return multi_polygon()
