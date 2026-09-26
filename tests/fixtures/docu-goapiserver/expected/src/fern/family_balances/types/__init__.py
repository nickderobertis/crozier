



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_family_balances_id_v3request_fields_item import GetFamilyBalancesIdV3RequestFieldsItem
    from .get_family_balances_v3request_fields_item import GetFamilyBalancesV3RequestFieldsItem
    from .get_family_balances_v3request_group_by import GetFamilyBalancesV3RequestGroupBy
    from .get_family_balances_v3request_metrics_item import GetFamilyBalancesV3RequestMetricsItem
    from .get_family_balances_v3request_view import GetFamilyBalancesV3RequestView
    from .get_family_balances_v3response import GetFamilyBalancesV3Response
_dynamic_imports: typing.Dict[str, str] = {
    "GetFamilyBalancesIdV3RequestFieldsItem": ".get_family_balances_id_v3request_fields_item",
    "GetFamilyBalancesV3RequestFieldsItem": ".get_family_balances_v3request_fields_item",
    "GetFamilyBalancesV3RequestGroupBy": ".get_family_balances_v3request_group_by",
    "GetFamilyBalancesV3RequestMetricsItem": ".get_family_balances_v3request_metrics_item",
    "GetFamilyBalancesV3RequestView": ".get_family_balances_v3request_view",
    "GetFamilyBalancesV3Response": ".get_family_balances_v3response",
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
    "GetFamilyBalancesIdV3RequestFieldsItem",
    "GetFamilyBalancesV3RequestFieldsItem",
    "GetFamilyBalancesV3RequestGroupBy",
    "GetFamilyBalancesV3RequestMetricsItem",
    "GetFamilyBalancesV3RequestView",
    "GetFamilyBalancesV3Response",
]
