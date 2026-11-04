



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .latest_v1get_v1latest_get_request_location_item import LatestV1GetV1LatestGetRequestLocationItem
    from .latest_v1get_v1latest_get_request_parameter_item import LatestV1GetV1LatestGetRequestParameterItem
    from .latest_v1get_v1latest_location_id_get_request_location_item import (
        LatestV1GetV1LatestLocationIdGetRequestLocationItem,
    )
    from .latest_v1get_v1latest_location_id_get_request_parameter_item import (
        LatestV1GetV1LatestLocationIdGetRequestParameterItem,
    )
    from .locationsv1get_v1locations_get_request_location_item import Locationsv1GetV1LocationsGetRequestLocationItem
    from .locationsv1get_v1locations_get_request_parameter_item import Locationsv1GetV1LocationsGetRequestParameterItem
    from .locationsv1get_v1locations_location_id_get_request_location_item import (
        Locationsv1GetV1LocationsLocationIdGetRequestLocationItem,
    )
    from .locationsv1get_v1locations_location_id_get_request_parameter_item import (
        Locationsv1GetV1LocationsLocationIdGetRequestParameterItem,
    )
    from .measurements_get_v1v1measurements_get_request_location_item import (
        MeasurementsGetV1V1MeasurementsGetRequestLocationItem,
    )
    from .measurements_get_v1v1measurements_get_request_parameter_item import (
        MeasurementsGetV1V1MeasurementsGetRequestParameterItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "LatestV1GetV1LatestGetRequestLocationItem": ".latest_v1get_v1latest_get_request_location_item",
    "LatestV1GetV1LatestGetRequestParameterItem": ".latest_v1get_v1latest_get_request_parameter_item",
    "LatestV1GetV1LatestLocationIdGetRequestLocationItem": ".latest_v1get_v1latest_location_id_get_request_location_item",
    "LatestV1GetV1LatestLocationIdGetRequestParameterItem": ".latest_v1get_v1latest_location_id_get_request_parameter_item",
    "Locationsv1GetV1LocationsGetRequestLocationItem": ".locationsv1get_v1locations_get_request_location_item",
    "Locationsv1GetV1LocationsGetRequestParameterItem": ".locationsv1get_v1locations_get_request_parameter_item",
    "Locationsv1GetV1LocationsLocationIdGetRequestLocationItem": ".locationsv1get_v1locations_location_id_get_request_location_item",
    "Locationsv1GetV1LocationsLocationIdGetRequestParameterItem": ".locationsv1get_v1locations_location_id_get_request_parameter_item",
    "MeasurementsGetV1V1MeasurementsGetRequestLocationItem": ".measurements_get_v1v1measurements_get_request_location_item",
    "MeasurementsGetV1V1MeasurementsGetRequestParameterItem": ".measurements_get_v1v1measurements_get_request_parameter_item",
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
    "LatestV1GetV1LatestGetRequestLocationItem",
    "LatestV1GetV1LatestGetRequestParameterItem",
    "LatestV1GetV1LatestLocationIdGetRequestLocationItem",
    "LatestV1GetV1LatestLocationIdGetRequestParameterItem",
    "Locationsv1GetV1LocationsGetRequestLocationItem",
    "Locationsv1GetV1LocationsGetRequestParameterItem",
    "Locationsv1GetV1LocationsLocationIdGetRequestLocationItem",
    "Locationsv1GetV1LocationsLocationIdGetRequestParameterItem",
    "MeasurementsGetV1V1MeasurementsGetRequestLocationItem",
    "MeasurementsGetV1V1MeasurementsGetRequestParameterItem",
]
