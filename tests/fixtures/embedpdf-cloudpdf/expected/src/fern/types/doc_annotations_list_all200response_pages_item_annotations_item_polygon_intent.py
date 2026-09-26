

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonIntent(enum.StrEnum):
    POLYGON_CLOUD = "PolygonCloud"
    POLYGON_DIMENSION = "PolygonDimension"

    def visit(
        self, polygon_cloud: typing.Callable[[], T_Result], polygon_dimension: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonIntent.POLYGON_CLOUD:
            return polygon_cloud()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonIntent.POLYGON_DIMENSION:
            return polygon_dimension()
