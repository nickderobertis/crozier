

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SimpleDataModelsGeoJsonGeometryTypeOneType(enum.StrEnum):
    LINE_STRING = "LineString"

    def visit(self, line_string: typing.Callable[[], T_Result]) -> T_Result:
        if self is SimpleDataModelsGeoJsonGeometryTypeOneType.LINE_STRING:
            return line_string()
