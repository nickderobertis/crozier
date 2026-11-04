



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .collection import Collection
    from .collections import Collections
    from .conf_classes import ConfClasses
    from .exception import Exception
    from .extent import Extent
    from .extent_spatial import ExtentSpatial
    from .extent_spatial_crs import ExtentSpatialCrs
    from .extent_temporal import ExtentTemporal
    from .extent_temporal_trs import ExtentTemporalTrs
    from .feature_collection_geo_json import FeatureCollectionGeoJson
    from .feature_collection_geo_json_type import FeatureCollectionGeoJsonType
    from .feature_geo_json import FeatureGeoJson
    from .feature_geo_json_id import FeatureGeoJsonId
    from .feature_geo_json_type import FeatureGeoJsonType
    from .geometry_geo_json import (
        GeometryGeoJson,
        GeometryGeoJson_GeometryCollection,
        GeometryGeoJson_LineString,
        GeometryGeoJson_MultiLineString,
        GeometryGeoJson_MultiPoint,
        GeometryGeoJson_MultiPolygon,
        GeometryGeoJson_Point,
        GeometryGeoJson_Polygon,
    )
    from .geometrycollection_geo_json import GeometrycollectionGeoJson
    from .landing_page import LandingPage
    from .linestring_geo_json import LinestringGeoJson
    from .link import Link
    from .multilinestring_geo_json import MultilinestringGeoJson
    from .multipoint_geo_json import MultipointGeoJson
    from .multipolygon_geo_json import MultipolygonGeoJson
    from .number_matched import NumberMatched
    from .number_returned import NumberReturned
    from .point_geo_json import PointGeoJson
    from .polygon_geo_json import PolygonGeoJson
    from .time_stamp import TimeStamp
_dynamic_imports: typing.Dict[str, str] = {
    "Collection": ".collection",
    "Collections": ".collections",
    "ConfClasses": ".conf_classes",
    "Exception": ".exception",
    "Extent": ".extent",
    "ExtentSpatial": ".extent_spatial",
    "ExtentSpatialCrs": ".extent_spatial_crs",
    "ExtentTemporal": ".extent_temporal",
    "ExtentTemporalTrs": ".extent_temporal_trs",
    "FeatureCollectionGeoJson": ".feature_collection_geo_json",
    "FeatureCollectionGeoJsonType": ".feature_collection_geo_json_type",
    "FeatureGeoJson": ".feature_geo_json",
    "FeatureGeoJsonId": ".feature_geo_json_id",
    "FeatureGeoJsonType": ".feature_geo_json_type",
    "GeometryGeoJson": ".geometry_geo_json",
    "GeometryGeoJson_GeometryCollection": ".geometry_geo_json",
    "GeometryGeoJson_LineString": ".geometry_geo_json",
    "GeometryGeoJson_MultiLineString": ".geometry_geo_json",
    "GeometryGeoJson_MultiPoint": ".geometry_geo_json",
    "GeometryGeoJson_MultiPolygon": ".geometry_geo_json",
    "GeometryGeoJson_Point": ".geometry_geo_json",
    "GeometryGeoJson_Polygon": ".geometry_geo_json",
    "GeometrycollectionGeoJson": ".geometrycollection_geo_json",
    "LandingPage": ".landing_page",
    "LinestringGeoJson": ".linestring_geo_json",
    "Link": ".link",
    "MultilinestringGeoJson": ".multilinestring_geo_json",
    "MultipointGeoJson": ".multipoint_geo_json",
    "MultipolygonGeoJson": ".multipolygon_geo_json",
    "NumberMatched": ".number_matched",
    "NumberReturned": ".number_returned",
    "PointGeoJson": ".point_geo_json",
    "PolygonGeoJson": ".polygon_geo_json",
    "TimeStamp": ".time_stamp",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "Collection",
    "Collections",
    "ConfClasses",
    "Exception",
    "Extent",
    "ExtentSpatial",
    "ExtentSpatialCrs",
    "ExtentTemporal",
    "ExtentTemporalTrs",
    "FeatureCollectionGeoJson",
    "FeatureCollectionGeoJsonType",
    "FeatureGeoJson",
    "FeatureGeoJsonId",
    "FeatureGeoJsonType",
    "GeometryGeoJson",
    "GeometryGeoJson_GeometryCollection",
    "GeometryGeoJson_LineString",
    "GeometryGeoJson_MultiLineString",
    "GeometryGeoJson_MultiPoint",
    "GeometryGeoJson_MultiPolygon",
    "GeometryGeoJson_Point",
    "GeometryGeoJson_Polygon",
    "GeometrycollectionGeoJson",
    "LandingPage",
    "LinestringGeoJson",
    "Link",
    "MultilinestringGeoJson",
    "MultipointGeoJson",
    "MultipolygonGeoJson",
    "NumberMatched",
    "NumberReturned",
    "PointGeoJson",
    "PolygonGeoJson",
    "TimeStamp",
]
