



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .abstract_any_crs_feature_collection import AbstractAnyCrsFeatureCollection
    from .abstract_bin_grid import AbstractBinGrid
    from .abstract_feature import AbstractFeature
    from .abstract_feature_collection import AbstractFeatureCollection
    from .abstract_spatial_location import AbstractSpatialLocation
    from .connected_outer_service import ConnectedOuterService
    from .convert_bin_grid_response import ConvertBinGridResponse
    from .convert_geo_json_request import ConvertGeoJsonRequest
    from .convert_geo_json_response import ConvertGeoJsonResponse
    from .convert_points_request import ConvertPointsRequest
    from .convert_points_response import ConvertPointsResponse
    from .convert_trajectory_request import ConvertTrajectoryRequest
    from .convert_trajectory_response import ConvertTrajectoryResponse
    from .geo_json_base import GeoJsonBase
    from .geo_json_base_geo_json_variant_internal import GeoJsonBaseGeoJsonVariantInternal
    from .geo_json_feature import GeoJsonFeature
    from .geo_json_feature_collection import GeoJsonFeatureCollection
    from .geo_json_feature_collection_geo_json_variant_internal import GeoJsonFeatureCollectionGeoJsonVariantInternal
    from .geo_json_feature_geo_json_variant_internal import GeoJsonFeatureGeoJsonVariantInternal
    from .geo_json_feature_geometry import GeoJsonFeatureGeometry
    from .geo_json_geometry_collection import GeoJsonGeometryCollection
    from .geo_json_line_string import GeoJsonLineString
    from .geo_json_multi_line_string import GeoJsonMultiLineString
    from .geo_json_multi_point import GeoJsonMultiPoint
    from .geo_json_multi_polygon import GeoJsonMultiPolygon
    from .geo_json_point import GeoJsonPoint
    from .geo_json_polygon import GeoJsonPolygon
    from .geometry import Geometry
    from .max_mis_location import MaxMisLocation
    from .point import Point
    from .point_properties import PointProperties
    from .properties_bin_grid_corners import PropertiesBinGridCorners
    from .trajectory_station_in import TrajectoryStationIn
    from .trajectory_station_out import TrajectoryStationOut
    from .version_info import VersionInfo
_dynamic_imports: typing.Dict[str, str] = {
    "AbstractAnyCrsFeatureCollection": ".abstract_any_crs_feature_collection",
    "AbstractBinGrid": ".abstract_bin_grid",
    "AbstractFeature": ".abstract_feature",
    "AbstractFeatureCollection": ".abstract_feature_collection",
    "AbstractSpatialLocation": ".abstract_spatial_location",
    "ConnectedOuterService": ".connected_outer_service",
    "ConvertBinGridResponse": ".convert_bin_grid_response",
    "ConvertGeoJsonRequest": ".convert_geo_json_request",
    "ConvertGeoJsonResponse": ".convert_geo_json_response",
    "ConvertPointsRequest": ".convert_points_request",
    "ConvertPointsResponse": ".convert_points_response",
    "ConvertTrajectoryRequest": ".convert_trajectory_request",
    "ConvertTrajectoryResponse": ".convert_trajectory_response",
    "GeoJsonBase": ".geo_json_base",
    "GeoJsonBaseGeoJsonVariantInternal": ".geo_json_base_geo_json_variant_internal",
    "GeoJsonFeature": ".geo_json_feature",
    "GeoJsonFeatureCollection": ".geo_json_feature_collection",
    "GeoJsonFeatureCollectionGeoJsonVariantInternal": ".geo_json_feature_collection_geo_json_variant_internal",
    "GeoJsonFeatureGeoJsonVariantInternal": ".geo_json_feature_geo_json_variant_internal",
    "GeoJsonFeatureGeometry": ".geo_json_feature_geometry",
    "GeoJsonGeometryCollection": ".geo_json_geometry_collection",
    "GeoJsonLineString": ".geo_json_line_string",
    "GeoJsonMultiLineString": ".geo_json_multi_line_string",
    "GeoJsonMultiPoint": ".geo_json_multi_point",
    "GeoJsonMultiPolygon": ".geo_json_multi_polygon",
    "GeoJsonPoint": ".geo_json_point",
    "GeoJsonPolygon": ".geo_json_polygon",
    "Geometry": ".geometry",
    "MaxMisLocation": ".max_mis_location",
    "Point": ".point",
    "PointProperties": ".point_properties",
    "PropertiesBinGridCorners": ".properties_bin_grid_corners",
    "TrajectoryStationIn": ".trajectory_station_in",
    "TrajectoryStationOut": ".trajectory_station_out",
    "VersionInfo": ".version_info",
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
    "ConnectedOuterService",
    "ConvertBinGridResponse",
    "ConvertGeoJsonRequest",
    "ConvertGeoJsonResponse",
    "ConvertPointsRequest",
    "ConvertPointsResponse",
    "ConvertTrajectoryRequest",
    "ConvertTrajectoryResponse",
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
]
