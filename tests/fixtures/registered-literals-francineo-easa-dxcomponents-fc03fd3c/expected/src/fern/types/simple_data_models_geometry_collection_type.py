

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SimpleDataModelsGeometryCollectionType(enum.StrEnum):
    GEOMETRY_COLLECTION = "GeometryCollection"

    def visit(self, geometry_collection: typing.Callable[[], T_Result]) -> T_Result:
        if self is SimpleDataModelsGeometryCollectionType.GEOMETRY_COLLECTION:
            return geometry_collection()
