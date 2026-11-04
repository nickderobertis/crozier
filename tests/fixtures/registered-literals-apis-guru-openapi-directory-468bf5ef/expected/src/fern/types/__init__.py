



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .averages_v2get_v2averages_get_request_date_from import AveragesV2GetV2AveragesGetRequestDateFrom
    from .averages_v2get_v2averages_get_request_date_to import AveragesV2GetV2AveragesGetRequestDateTo
    from .cities_order import CitiesOrder
    from .cities_row import CitiesRow
    from .countries_order import CountriesOrder
    from .countries_row import CountriesRow
    from .entity_types import EntityTypes
    from .get_mobilegentile_v2locations_tiles_mobile_generalized_zxy_pbf_get_request_last_updated_from import (
        GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedFrom,
    )
    from .get_mobilegentile_v2locations_tiles_mobile_generalized_zxy_pbf_get_request_last_updated_to import (
        GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedTo,
    )
    from .get_mobilegentile_v2locations_tiles_mobile_generalized_zxy_pbf_get_request_parameter import (
        GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestParameter,
    )
    from .get_mobiletile_v2locations_tiles_mobile_zxy_pbf_get_request_last_updated_from import (
        GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedFrom,
    )
    from .get_mobiletile_v2locations_tiles_mobile_zxy_pbf_get_request_last_updated_to import (
        GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedTo,
    )
    from .get_mobiletile_v2locations_tiles_mobile_zxy_pbf_get_request_parameter import (
        GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestParameter,
    )
    from .get_tile_v2locations_tiles_zxy_pbf_get_request_last_updated_from import (
        GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedFrom,
    )
    from .get_tile_v2locations_tiles_zxy_pbf_get_request_last_updated_to import (
        GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedTo,
    )
    from .get_tile_v2locations_tiles_zxy_pbf_get_request_parameter import (
        GetTileV2LocationsTilesZxyPbfGetRequestParameter,
    )
    from .http_validation_error import HttpValidationError
    from .locations_order import LocationsOrder
    from .meas_order import MeasOrder
    from .measurements_get_v1v1measurements_get_request_date_from import (
        MeasurementsGetV1V1MeasurementsGetRequestDateFrom,
    )
    from .measurements_get_v1v1measurements_get_request_date_to import MeasurementsGetV1V1MeasurementsGetRequestDateTo
    from .measurements_get_v2measurements_get_request_date_from import MeasurementsGetV2MeasurementsGetRequestDateFrom
    from .measurements_get_v2measurements_get_request_date_to import MeasurementsGetV2MeasurementsGetRequestDateTo
    from .meta import Meta
    from .open_aq_cities_result import OpenAqCitiesResult
    from .open_aq_countries_result import OpenAqCountriesResult
    from .open_aq_parameters_result import OpenAqParametersResult
    from .open_aq_projects_result import OpenAqProjectsResult
    from .open_aq_result import OpenAqResult
    from .parameters_row import ParametersRow
    from .project_parameter_details import ProjectParameterDetails
    from .projects_order import ProjectsOrder
    from .projects_row import ProjectsRow
    from .sensor_types import SensorTypes
    from .sort import Sort
    from .sources_order import SourcesOrder
    from .sources_v1order import SourcesV1Order
    from .spatial import Spatial
    from .temporal import Temporal
    from .tile_json import TileJson
    from .validation_error import ValidationError
_dynamic_imports: typing.Dict[str, str] = {
    "AveragesV2GetV2AveragesGetRequestDateFrom": ".averages_v2get_v2averages_get_request_date_from",
    "AveragesV2GetV2AveragesGetRequestDateTo": ".averages_v2get_v2averages_get_request_date_to",
    "CitiesOrder": ".cities_order",
    "CitiesRow": ".cities_row",
    "CountriesOrder": ".countries_order",
    "CountriesRow": ".countries_row",
    "EntityTypes": ".entity_types",
    "GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedFrom": ".get_mobilegentile_v2locations_tiles_mobile_generalized_zxy_pbf_get_request_last_updated_from",
    "GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedTo": ".get_mobilegentile_v2locations_tiles_mobile_generalized_zxy_pbf_get_request_last_updated_to",
    "GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestParameter": ".get_mobilegentile_v2locations_tiles_mobile_generalized_zxy_pbf_get_request_parameter",
    "GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedFrom": ".get_mobiletile_v2locations_tiles_mobile_zxy_pbf_get_request_last_updated_from",
    "GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedTo": ".get_mobiletile_v2locations_tiles_mobile_zxy_pbf_get_request_last_updated_to",
    "GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestParameter": ".get_mobiletile_v2locations_tiles_mobile_zxy_pbf_get_request_parameter",
    "GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedFrom": ".get_tile_v2locations_tiles_zxy_pbf_get_request_last_updated_from",
    "GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedTo": ".get_tile_v2locations_tiles_zxy_pbf_get_request_last_updated_to",
    "GetTileV2LocationsTilesZxyPbfGetRequestParameter": ".get_tile_v2locations_tiles_zxy_pbf_get_request_parameter",
    "HttpValidationError": ".http_validation_error",
    "LocationsOrder": ".locations_order",
    "MeasOrder": ".meas_order",
    "MeasurementsGetV1V1MeasurementsGetRequestDateFrom": ".measurements_get_v1v1measurements_get_request_date_from",
    "MeasurementsGetV1V1MeasurementsGetRequestDateTo": ".measurements_get_v1v1measurements_get_request_date_to",
    "MeasurementsGetV2MeasurementsGetRequestDateFrom": ".measurements_get_v2measurements_get_request_date_from",
    "MeasurementsGetV2MeasurementsGetRequestDateTo": ".measurements_get_v2measurements_get_request_date_to",
    "Meta": ".meta",
    "OpenAqCitiesResult": ".open_aq_cities_result",
    "OpenAqCountriesResult": ".open_aq_countries_result",
    "OpenAqParametersResult": ".open_aq_parameters_result",
    "OpenAqProjectsResult": ".open_aq_projects_result",
    "OpenAqResult": ".open_aq_result",
    "ParametersRow": ".parameters_row",
    "ProjectParameterDetails": ".project_parameter_details",
    "ProjectsOrder": ".projects_order",
    "ProjectsRow": ".projects_row",
    "SensorTypes": ".sensor_types",
    "Sort": ".sort",
    "SourcesOrder": ".sources_order",
    "SourcesV1Order": ".sources_v1order",
    "Spatial": ".spatial",
    "Temporal": ".temporal",
    "TileJson": ".tile_json",
    "ValidationError": ".validation_error",
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
    "AveragesV2GetV2AveragesGetRequestDateFrom",
    "AveragesV2GetV2AveragesGetRequestDateTo",
    "CitiesOrder",
    "CitiesRow",
    "CountriesOrder",
    "CountriesRow",
    "EntityTypes",
    "GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedFrom",
    "GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestLastUpdatedTo",
    "GetMobilegentileV2LocationsTilesMobileGeneralizedZxyPbfGetRequestParameter",
    "GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedFrom",
    "GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestLastUpdatedTo",
    "GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestParameter",
    "GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedFrom",
    "GetTileV2LocationsTilesZxyPbfGetRequestLastUpdatedTo",
    "GetTileV2LocationsTilesZxyPbfGetRequestParameter",
    "HttpValidationError",
    "LocationsOrder",
    "MeasOrder",
    "MeasurementsGetV1V1MeasurementsGetRequestDateFrom",
    "MeasurementsGetV1V1MeasurementsGetRequestDateTo",
    "MeasurementsGetV2MeasurementsGetRequestDateFrom",
    "MeasurementsGetV2MeasurementsGetRequestDateTo",
    "Meta",
    "OpenAqCitiesResult",
    "OpenAqCountriesResult",
    "OpenAqParametersResult",
    "OpenAqProjectsResult",
    "OpenAqResult",
    "ParametersRow",
    "ProjectParameterDetails",
    "ProjectsOrder",
    "ProjectsRow",
    "SensorTypes",
    "Sort",
    "SourcesOrder",
    "SourcesV1Order",
    "Spatial",
    "Temporal",
    "TileJson",
    "ValidationError",
]
