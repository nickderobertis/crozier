

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SimpleDataModelsGeoJsonGeometryTypeTwoType(enum.StrEnum):
    POLYGON = "Polygon"

    def visit(self, polygon: typing.Callable[[], T_Result]) -> T_Result:
        if self is SimpleDataModelsGeoJsonGeometryTypeTwoType.POLYGON:
            return polygon()
