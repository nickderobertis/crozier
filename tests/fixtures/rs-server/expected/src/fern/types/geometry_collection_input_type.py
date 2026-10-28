

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GeometryCollectionInputType(enum.StrEnum):
    GEOMETRY_COLLECTION = "GeometryCollection"

    def visit(self, geometry_collection: typing.Callable[[], T_Result]) -> T_Result:
        if self is GeometryCollectionInputType.GEOMETRY_COLLECTION:
            return geometry_collection()
