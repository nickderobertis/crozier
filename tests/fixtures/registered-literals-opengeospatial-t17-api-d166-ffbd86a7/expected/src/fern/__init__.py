



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Collection,
        Collections,
        ConfClasses,
        Exception,
        Extent,
        ExtentSpatial,
        ExtentSpatialCrs,
        ExtentTemporal,
        ExtentTemporalTrs,
        FeatureCollectionGeoJson,
        FeatureCollectionGeoJsonType,
        FeatureGeoJson,
        FeatureGeoJsonId,
        FeatureGeoJsonType,
        GeometryGeoJson,
        GeometryGeoJson_GeometryCollection,
        GeometryGeoJson_LineString,
        GeometryGeoJson_MultiLineString,
        GeometryGeoJson_MultiPoint,
        GeometryGeoJson_MultiPolygon,
        GeometryGeoJson_Point,
        GeometryGeoJson_Polygon,
        GeometrycollectionGeoJson,
        LandingPage,
        LinestringGeoJson,
        Link,
        MultilinestringGeoJson,
        MultipointGeoJson,
        MultipolygonGeoJson,
        NumberMatched,
        NumberReturned,
        PointGeoJson,
        PolygonGeoJson,
        TimeStamp,
    )
    from .errors import BadRequestError, InternalServerError, NotFoundError
    from . import capabilities, data
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "Collection": ".types",
    "Collections": ".types",
    "ConfClasses": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Exception": ".types",
    "Extent": ".types",
    "ExtentSpatial": ".types",
    "ExtentSpatialCrs": ".types",
    "ExtentTemporal": ".types",
    "ExtentTemporalTrs": ".types",
    "FeatureCollectionGeoJson": ".types",
    "FeatureCollectionGeoJsonType": ".types",
    "FeatureGeoJson": ".types",
    "FeatureGeoJsonId": ".types",
    "FeatureGeoJsonType": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GeometryGeoJson": ".types",
    "GeometryGeoJson_GeometryCollection": ".types",
    "GeometryGeoJson_LineString": ".types",
    "GeometryGeoJson_MultiLineString": ".types",
    "GeometryGeoJson_MultiPoint": ".types",
    "GeometryGeoJson_MultiPolygon": ".types",
    "GeometryGeoJson_Point": ".types",
    "GeometryGeoJson_Polygon": ".types",
    "GeometrycollectionGeoJson": ".types",
    "InternalServerError": ".errors",
    "LandingPage": ".types",
    "LinestringGeoJson": ".types",
    "Link": ".types",
    "MultilinestringGeoJson": ".types",
    "MultipointGeoJson": ".types",
    "MultipolygonGeoJson": ".types",
    "NotFoundError": ".errors",
    "NumberMatched": ".types",
    "NumberReturned": ".types",
    "PointGeoJson": ".types",
    "PolygonGeoJson": ".types",
    "TimeStamp": ".types",
    "__version__": ".version",
    "capabilities": ".capabilities",
    "data": ".data",
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
    "AsyncFernApi",
    "BadRequestError",
    "Collection",
    "Collections",
    "ConfClasses",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
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
    "FernApi",
    "FernApiEnvironment",
    "GeometryGeoJson",
    "GeometryGeoJson_GeometryCollection",
    "GeometryGeoJson_LineString",
    "GeometryGeoJson_MultiLineString",
    "GeometryGeoJson_MultiPoint",
    "GeometryGeoJson_MultiPolygon",
    "GeometryGeoJson_Point",
    "GeometryGeoJson_Polygon",
    "GeometrycollectionGeoJson",
    "InternalServerError",
    "LandingPage",
    "LinestringGeoJson",
    "Link",
    "MultilinestringGeoJson",
    "MultipointGeoJson",
    "MultipolygonGeoJson",
    "NotFoundError",
    "NumberMatched",
    "NumberReturned",
    "PointGeoJson",
    "PolygonGeoJson",
    "TimeStamp",
    "__version__",
    "capabilities",
    "data",
]
