



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AbstractAnyCrsFeatureCollection,
        AbstractBinGrid,
        AbstractFeature,
        AbstractFeatureCollection,
        AbstractSpatialLocation,
        ConnectedOuterService,
        ConvertBinGridResponse,
        ConvertGeoJsonRequest,
        ConvertGeoJsonResponse,
        ConvertPointsRequest,
        ConvertPointsResponse,
        ConvertTrajectoryRequest,
        ConvertTrajectoryResponse,
        GeoJsonBase,
        GeoJsonBaseGeoJsonVariantInternal,
        GeoJsonFeature,
        GeoJsonFeatureCollection,
        GeoJsonFeatureCollectionGeoJsonVariantInternal,
        GeoJsonFeatureGeoJsonVariantInternal,
        GeoJsonFeatureGeometry,
        GeoJsonGeometryCollection,
        GeoJsonLineString,
        GeoJsonMultiLineString,
        GeoJsonMultiPoint,
        GeoJsonMultiPolygon,
        GeoJsonPoint,
        GeoJsonPolygon,
        Geometry,
        MaxMisLocation,
        Point,
        PointProperties,
        PropertiesBinGridCorners,
        TrajectoryStationIn,
        TrajectoryStationOut,
        VersionInfo,
    )
    from . import crs_converter_api_v2, crs_converter_api_v3, health_check, info_api
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AbstractAnyCrsFeatureCollection": ".types",
    "AbstractBinGrid": ".types",
    "AbstractFeature": ".types",
    "AbstractFeatureCollection": ".types",
    "AbstractSpatialLocation": ".types",
    "AsyncFernApi": ".client",
    "ConnectedOuterService": ".types",
    "ConvertBinGridResponse": ".types",
    "ConvertGeoJsonRequest": ".types",
    "ConvertGeoJsonResponse": ".types",
    "ConvertPointsRequest": ".types",
    "ConvertPointsResponse": ".types",
    "ConvertTrajectoryRequest": ".types",
    "ConvertTrajectoryResponse": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GeoJsonBase": ".types",
    "GeoJsonBaseGeoJsonVariantInternal": ".types",
    "GeoJsonFeature": ".types",
    "GeoJsonFeatureCollection": ".types",
    "GeoJsonFeatureCollectionGeoJsonVariantInternal": ".types",
    "GeoJsonFeatureGeoJsonVariantInternal": ".types",
    "GeoJsonFeatureGeometry": ".types",
    "GeoJsonGeometryCollection": ".types",
    "GeoJsonLineString": ".types",
    "GeoJsonMultiLineString": ".types",
    "GeoJsonMultiPoint": ".types",
    "GeoJsonMultiPolygon": ".types",
    "GeoJsonPoint": ".types",
    "GeoJsonPolygon": ".types",
    "Geometry": ".types",
    "MaxMisLocation": ".types",
    "Point": ".types",
    "PointProperties": ".types",
    "PropertiesBinGridCorners": ".types",
    "TrajectoryStationIn": ".types",
    "TrajectoryStationOut": ".types",
    "VersionInfo": ".types",
    "__version__": ".version",
    "crs_converter_api_v2": ".crs_converter_api_v2",
    "crs_converter_api_v3": ".crs_converter_api_v3",
    "health_check": ".health_check",
    "info_api": ".info_api",
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
    "AbstractAnyCrsFeatureCollection",
    "AbstractBinGrid",
    "AbstractFeature",
    "AbstractFeatureCollection",
    "AbstractSpatialLocation",
    "AsyncFernApi",
    "ConnectedOuterService",
    "ConvertBinGridResponse",
    "ConvertGeoJsonRequest",
    "ConvertGeoJsonResponse",
    "ConvertPointsRequest",
    "ConvertPointsResponse",
    "ConvertTrajectoryRequest",
    "ConvertTrajectoryResponse",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "GeoJsonBase",
    "GeoJsonBaseGeoJsonVariantInternal",
    "GeoJsonFeature",
    "GeoJsonFeatureCollection",
    "GeoJsonFeatureCollectionGeoJsonVariantInternal",
    "GeoJsonFeatureGeoJsonVariantInternal",
    "GeoJsonFeatureGeometry",
    "GeoJsonGeometryCollection",
    "GeoJsonLineString",
    "GeoJsonMultiLineString",
    "GeoJsonMultiPoint",
    "GeoJsonMultiPolygon",
    "GeoJsonPoint",
    "GeoJsonPolygon",
    "Geometry",
    "MaxMisLocation",
    "Point",
    "PointProperties",
    "PropertiesBinGridCorners",
    "TrajectoryStationIn",
    "TrajectoryStationOut",
    "VersionInfo",
    "__version__",
    "crs_converter_api_v2",
    "crs_converter_api_v3",
    "health_check",
    "info_api",
]
