



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .averages_v2get_v2averages_get_request_parameter_item import AveragesV2GetV2AveragesGetRequestParameterItem
    from .averages_v2get_v2averages_get_request_project_item import AveragesV2GetV2AveragesGetRequestProjectItem
    from .get_mobiletile_v2locations_tiles_mobile_zxy_pbf_get_request_date_from import (
        GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateFrom,
    )
    from .get_mobiletile_v2locations_tiles_mobile_zxy_pbf_get_request_date_to import (
        GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateTo,
    )
    from .latest_get_v2latest_get_request_location_item import LatestGetV2LatestGetRequestLocationItem
    from .latest_get_v2latest_get_request_parameter_item import LatestGetV2LatestGetRequestParameterItem
    from .latest_get_v2latest_location_id_get_request_location_item import (
        LatestGetV2LatestLocationIdGetRequestLocationItem,
    )
    from .latest_get_v2latest_location_id_get_request_parameter_item import (
        LatestGetV2LatestLocationIdGetRequestParameterItem,
    )
    from .locations_get_v2locations_get_request_location_item import LocationsGetV2LocationsGetRequestLocationItem
    from .locations_get_v2locations_get_request_parameter_item import LocationsGetV2LocationsGetRequestParameterItem
    from .locations_get_v2locations_location_id_get_request_location_item import (
        LocationsGetV2LocationsLocationIdGetRequestLocationItem,
    )
    from .locations_get_v2locations_location_id_get_request_parameter_item import (
        LocationsGetV2LocationsLocationIdGetRequestParameterItem,
    )
    from .measurements_get_v2measurements_get_request_location_item import (
        MeasurementsGetV2MeasurementsGetRequestLocationItem,
    )
    from .measurements_get_v2measurements_get_request_parameter_item import (
        MeasurementsGetV2MeasurementsGetRequestParameterItem,
    )
    from .projects_get_v2projects_get_request_parameter_item import ProjectsGetV2ProjectsGetRequestParameterItem
    from .projects_get_v2projects_get_request_project_item import ProjectsGetV2ProjectsGetRequestProjectItem
    from .projects_get_v2projects_project_id_get_request_parameter_item import (
        ProjectsGetV2ProjectsProjectIdGetRequestParameterItem,
    )
    from .projects_get_v2projects_project_id_get_request_project_item import (
        ProjectsGetV2ProjectsProjectIdGetRequestProjectItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "AveragesV2GetV2AveragesGetRequestParameterItem": ".averages_v2get_v2averages_get_request_parameter_item",
    "AveragesV2GetV2AveragesGetRequestProjectItem": ".averages_v2get_v2averages_get_request_project_item",
    "GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateFrom": ".get_mobiletile_v2locations_tiles_mobile_zxy_pbf_get_request_date_from",
    "GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateTo": ".get_mobiletile_v2locations_tiles_mobile_zxy_pbf_get_request_date_to",
    "LatestGetV2LatestGetRequestLocationItem": ".latest_get_v2latest_get_request_location_item",
    "LatestGetV2LatestGetRequestParameterItem": ".latest_get_v2latest_get_request_parameter_item",
    "LatestGetV2LatestLocationIdGetRequestLocationItem": ".latest_get_v2latest_location_id_get_request_location_item",
    "LatestGetV2LatestLocationIdGetRequestParameterItem": ".latest_get_v2latest_location_id_get_request_parameter_item",
    "LocationsGetV2LocationsGetRequestLocationItem": ".locations_get_v2locations_get_request_location_item",
    "LocationsGetV2LocationsGetRequestParameterItem": ".locations_get_v2locations_get_request_parameter_item",
    "LocationsGetV2LocationsLocationIdGetRequestLocationItem": ".locations_get_v2locations_location_id_get_request_location_item",
    "LocationsGetV2LocationsLocationIdGetRequestParameterItem": ".locations_get_v2locations_location_id_get_request_parameter_item",
    "MeasurementsGetV2MeasurementsGetRequestLocationItem": ".measurements_get_v2measurements_get_request_location_item",
    "MeasurementsGetV2MeasurementsGetRequestParameterItem": ".measurements_get_v2measurements_get_request_parameter_item",
    "ProjectsGetV2ProjectsGetRequestParameterItem": ".projects_get_v2projects_get_request_parameter_item",
    "ProjectsGetV2ProjectsGetRequestProjectItem": ".projects_get_v2projects_get_request_project_item",
    "ProjectsGetV2ProjectsProjectIdGetRequestParameterItem": ".projects_get_v2projects_project_id_get_request_parameter_item",
    "ProjectsGetV2ProjectsProjectIdGetRequestProjectItem": ".projects_get_v2projects_project_id_get_request_project_item",
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
    "AveragesV2GetV2AveragesGetRequestParameterItem",
    "AveragesV2GetV2AveragesGetRequestProjectItem",
    "GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateFrom",
    "GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateTo",
    "LatestGetV2LatestGetRequestLocationItem",
    "LatestGetV2LatestGetRequestParameterItem",
    "LatestGetV2LatestLocationIdGetRequestLocationItem",
    "LatestGetV2LatestLocationIdGetRequestParameterItem",
    "LocationsGetV2LocationsGetRequestLocationItem",
    "LocationsGetV2LocationsGetRequestParameterItem",
    "LocationsGetV2LocationsLocationIdGetRequestLocationItem",
    "LocationsGetV2LocationsLocationIdGetRequestParameterItem",
    "MeasurementsGetV2MeasurementsGetRequestLocationItem",
    "MeasurementsGetV2MeasurementsGetRequestParameterItem",
    "ProjectsGetV2ProjectsGetRequestParameterItem",
    "ProjectsGetV2ProjectsGetRequestProjectItem",
    "ProjectsGetV2ProjectsProjectIdGetRequestParameterItem",
    "ProjectsGetV2ProjectsProjectIdGetRequestProjectItem",
]
