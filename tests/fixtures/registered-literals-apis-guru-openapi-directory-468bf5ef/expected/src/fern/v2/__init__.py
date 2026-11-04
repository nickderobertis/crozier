



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AveragesV2GetV2AveragesGetRequestParameterItem,
        AveragesV2GetV2AveragesGetRequestProjectItem,
        GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateFrom,
        GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateTo,
        LatestGetV2LatestGetRequestLocationItem,
        LatestGetV2LatestGetRequestParameterItem,
        LatestGetV2LatestLocationIdGetRequestLocationItem,
        LatestGetV2LatestLocationIdGetRequestParameterItem,
        LocationsGetV2LocationsGetRequestLocationItem,
        LocationsGetV2LocationsGetRequestParameterItem,
        LocationsGetV2LocationsLocationIdGetRequestLocationItem,
        LocationsGetV2LocationsLocationIdGetRequestParameterItem,
        MeasurementsGetV2MeasurementsGetRequestLocationItem,
        MeasurementsGetV2MeasurementsGetRequestParameterItem,
        ProjectsGetV2ProjectsGetRequestParameterItem,
        ProjectsGetV2ProjectsGetRequestProjectItem,
        ProjectsGetV2ProjectsProjectIdGetRequestParameterItem,
        ProjectsGetV2ProjectsProjectIdGetRequestProjectItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "AveragesV2GetV2AveragesGetRequestParameterItem": ".types",
    "AveragesV2GetV2AveragesGetRequestProjectItem": ".types",
    "GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateFrom": ".types",
    "GetMobiletileV2LocationsTilesMobileZxyPbfGetRequestDateTo": ".types",
    "LatestGetV2LatestGetRequestLocationItem": ".types",
    "LatestGetV2LatestGetRequestParameterItem": ".types",
    "LatestGetV2LatestLocationIdGetRequestLocationItem": ".types",
    "LatestGetV2LatestLocationIdGetRequestParameterItem": ".types",
    "LocationsGetV2LocationsGetRequestLocationItem": ".types",
    "LocationsGetV2LocationsGetRequestParameterItem": ".types",
    "LocationsGetV2LocationsLocationIdGetRequestLocationItem": ".types",
    "LocationsGetV2LocationsLocationIdGetRequestParameterItem": ".types",
    "MeasurementsGetV2MeasurementsGetRequestLocationItem": ".types",
    "MeasurementsGetV2MeasurementsGetRequestParameterItem": ".types",
    "ProjectsGetV2ProjectsGetRequestParameterItem": ".types",
    "ProjectsGetV2ProjectsGetRequestProjectItem": ".types",
    "ProjectsGetV2ProjectsProjectIdGetRequestParameterItem": ".types",
    "ProjectsGetV2ProjectsProjectIdGetRequestProjectItem": ".types",
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
