



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_spaces_detailed_list_v3request_fields_item import GetSpacesDetailedListV3RequestFieldsItem
    from .get_spaces_detailed_list_v3request_group_by import GetSpacesDetailedListV3RequestGroupBy
    from .get_spaces_detailed_list_v3request_metrics_item import GetSpacesDetailedListV3RequestMetricsItem
    from .get_spaces_detailed_list_v3request_view import GetSpacesDetailedListV3RequestView
    from .get_spaces_detailed_list_v3response import GetSpacesDetailedListV3Response
_dynamic_imports: typing.Dict[str, str] = {
    "GetSpacesDetailedListV3RequestFieldsItem": ".get_spaces_detailed_list_v3request_fields_item",
    "GetSpacesDetailedListV3RequestGroupBy": ".get_spaces_detailed_list_v3request_group_by",
    "GetSpacesDetailedListV3RequestMetricsItem": ".get_spaces_detailed_list_v3request_metrics_item",
    "GetSpacesDetailedListV3RequestView": ".get_spaces_detailed_list_v3request_view",
    "GetSpacesDetailedListV3Response": ".get_spaces_detailed_list_v3response",
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
    "GetSpacesDetailedListV3RequestFieldsItem",
    "GetSpacesDetailedListV3RequestGroupBy",
    "GetSpacesDetailedListV3RequestMetricsItem",
    "GetSpacesDetailedListV3RequestView",
    "GetSpacesDetailedListV3Response",
]
