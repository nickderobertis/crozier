

from __future__ import annotations

import typing

from .geo_json_geometry_collection import GeoJsonGeometryCollection
from .geo_json_line_string import GeoJsonLineString
from .geo_json_multi_line_string import GeoJsonMultiLineString
from .geo_json_multi_point import GeoJsonMultiPoint
from .geo_json_multi_polygon import GeoJsonMultiPolygon
from .geo_json_point import GeoJsonPoint
from .geo_json_polygon import GeoJsonPolygon

if typing.TYPE_CHECKING:
    from .geo_json_feature import GeoJsonFeature
    from .geo_json_feature_collection import GeoJsonFeatureCollection
GeoJsonFeatureGeometry = typing.Union[
    "GeoJsonFeature",
    "GeoJsonFeatureCollection",
    GeoJsonGeometryCollection,
    GeoJsonLineString,
    GeoJsonMultiLineString,
    GeoJsonMultiPoint,
    GeoJsonMultiPolygon,
    GeoJsonPoint,
    GeoJsonPolygon,
]
