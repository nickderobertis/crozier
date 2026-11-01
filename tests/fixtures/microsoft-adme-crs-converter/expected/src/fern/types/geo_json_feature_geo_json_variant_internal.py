

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GeoJsonFeatureGeoJsonVariantInternal(enum.StrEnum):
    GEO_JSON = "GEO_JSON"
    ANY_CRS_GEO_JSON = "ANY_CRS_GEO_JSON"

    def visit(
        self, geo_json: typing.Callable[[], T_Result], any_crs_geo_json: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is GeoJsonFeatureGeoJsonVariantInternal.GEO_JSON:
            return geo_json()
        if self is GeoJsonFeatureGeoJsonVariantInternal.ANY_CRS_GEO_JSON:
            return any_crs_geo_json()
