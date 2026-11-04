



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .accounts_abis_response import AccountsAbisResponse
    from .accounts_abis_response_data_item import AccountsAbisResponseDataItem
    from .accounts_export_request_flow import AccountsExportRequestFlow
    from .accounts_export_response import AccountsExportResponse
    from .accounts_export_response_data_item import AccountsExportResponseDataItem
    from .accounts_list_response import AccountsListResponse
    from .accounts_list_response_data_item import AccountsListResponseDataItem
    from .accounts_monitors_response import AccountsMonitorsResponse
    from .accounts_monitors_response_data_item import AccountsMonitorsResponseDataItem
    from .accounts_names_response import AccountsNamesResponse
    from .accounts_names_response_data_item import AccountsNamesResponseDataItem
_dynamic_imports: typing.Dict[str, str] = {
    "AccountsAbisResponse": ".accounts_abis_response",
    "AccountsAbisResponseDataItem": ".accounts_abis_response_data_item",
    "AccountsExportRequestFlow": ".accounts_export_request_flow",
    "AccountsExportResponse": ".accounts_export_response",
    "AccountsExportResponseDataItem": ".accounts_export_response_data_item",
    "AccountsListResponse": ".accounts_list_response",
    "AccountsListResponseDataItem": ".accounts_list_response_data_item",
    "AccountsMonitorsResponse": ".accounts_monitors_response",
    "AccountsMonitorsResponseDataItem": ".accounts_monitors_response_data_item",
    "AccountsNamesResponse": ".accounts_names_response",
    "AccountsNamesResponseDataItem": ".accounts_names_response_data_item",
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
    "AccountsAbisResponse",
    "AccountsAbisResponseDataItem",
    "AccountsExportRequestFlow",
    "AccountsExportResponse",
    "AccountsExportResponseDataItem",
    "AccountsListResponse",
    "AccountsListResponseDataItem",
    "AccountsMonitorsResponse",
    "AccountsMonitorsResponseDataItem",
    "AccountsNamesResponse",
    "AccountsNamesResponseDataItem",
]
