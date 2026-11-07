



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        LatestV1GetV1LatestGetRequestLocationItem,
        LatestV1GetV1LatestGetRequestParameterItem,
        LatestV1GetV1LatestLocationIdGetRequestLocationItem,
        LatestV1GetV1LatestLocationIdGetRequestParameterItem,
        Locationsv1GetV1LocationsGetRequestLocationItem,
        Locationsv1GetV1LocationsGetRequestParameterItem,
        Locationsv1GetV1LocationsLocationIdGetRequestLocationItem,
        Locationsv1GetV1LocationsLocationIdGetRequestParameterItem,
        MeasurementsGetV1V1MeasurementsGetRequestLocationItem,
        MeasurementsGetV1V1MeasurementsGetRequestParameterItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "LatestV1GetV1LatestGetRequestLocationItem": ".types",
    "LatestV1GetV1LatestGetRequestParameterItem": ".types",
    "LatestV1GetV1LatestLocationIdGetRequestLocationItem": ".types",
    "LatestV1GetV1LatestLocationIdGetRequestParameterItem": ".types",
    "Locationsv1GetV1LocationsGetRequestLocationItem": ".types",
    "Locationsv1GetV1LocationsGetRequestParameterItem": ".types",
    "Locationsv1GetV1LocationsLocationIdGetRequestLocationItem": ".types",
    "Locationsv1GetV1LocationsLocationIdGetRequestParameterItem": ".types",
    "MeasurementsGetV1V1MeasurementsGetRequestLocationItem": ".types",
    "MeasurementsGetV1V1MeasurementsGetRequestParameterItem": ".types",
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
