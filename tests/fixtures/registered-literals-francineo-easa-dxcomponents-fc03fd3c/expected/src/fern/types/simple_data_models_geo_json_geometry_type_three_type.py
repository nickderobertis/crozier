

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SimpleDataModelsGeoJsonGeometryTypeThreeType(enum.StrEnum):
    MULTI_POINT = "MultiPoint"

    def visit(self, multi_point: typing.Callable[[], T_Result]) -> T_Result:
        if self is SimpleDataModelsGeoJsonGeometryTypeThreeType.MULTI_POINT:
            return multi_point()
