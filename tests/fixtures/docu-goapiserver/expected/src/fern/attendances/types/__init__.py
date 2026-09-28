



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_attendances_v3request_fields_item import GetAttendancesV3RequestFieldsItem
    from .get_attendances_v3request_group_by import GetAttendancesV3RequestGroupBy
    from .get_attendances_v3request_metrics_item import GetAttendancesV3RequestMetricsItem
    from .get_attendances_v3request_sort_by import GetAttendancesV3RequestSortBy
    from .get_attendances_v3response import GetAttendancesV3Response
_dynamic_imports: typing.Dict[str, str] = {
    "GetAttendancesV3RequestFieldsItem": ".get_attendances_v3request_fields_item",
    "GetAttendancesV3RequestGroupBy": ".get_attendances_v3request_group_by",
    "GetAttendancesV3RequestMetricsItem": ".get_attendances_v3request_metrics_item",
    "GetAttendancesV3RequestSortBy": ".get_attendances_v3request_sort_by",
    "GetAttendancesV3Response": ".get_attendances_v3response",
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
    "GetAttendancesV3RequestFieldsItem",
    "GetAttendancesV3RequestGroupBy",
    "GetAttendancesV3RequestMetricsItem",
    "GetAttendancesV3RequestSortBy",
    "GetAttendancesV3Response",
]
