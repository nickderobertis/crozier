



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .catalog_category import CatalogCategory
    from .catalog_group import CatalogGroup
    from .catalog_name import CatalogName
    from .data_status import DataStatus
    from .evidance_data import EvidanceData
    from .executable import Executable
    from .get_response import GetResponse
    from .i_resolved_catalog import IResolvedCatalog
    from .i_resolved_source import IResolvedSource
    from .i_scan import IScan
    from .insight import Insight
    from .ivcs_installed_app import IvcsInstalledApp
    from .ivcs_installed_app_type import IvcsInstalledAppType
    from .ivcs_webhook import IvcsWebhook
    from .ivcs_webhook_type import IvcsWebhookType
    from .labels import Labels
    from .parsed_inventory import ParsedInventory
    from .parsed_inventory_sources_item import ParsedInventorySourcesItem
    from .parsed_inventory_sources_item_arguments import ParsedInventorySourcesItemArguments
    from .parsed_inventory_sources_item_arguments_one_item import ParsedInventorySourcesItemArgumentsOneItem
    from .source_name import SourceName
_dynamic_imports: typing.Dict[str, str] = {
    "CatalogCategory": ".catalog_category",
    "CatalogGroup": ".catalog_group",
    "CatalogName": ".catalog_name",
    "DataStatus": ".data_status",
    "EvidanceData": ".evidance_data",
    "Executable": ".executable",
    "GetResponse": ".get_response",
    "IResolvedCatalog": ".i_resolved_catalog",
    "IResolvedSource": ".i_resolved_source",
    "IScan": ".i_scan",
    "Insight": ".insight",
    "IvcsInstalledApp": ".ivcs_installed_app",
    "IvcsInstalledAppType": ".ivcs_installed_app_type",
    "IvcsWebhook": ".ivcs_webhook",
    "IvcsWebhookType": ".ivcs_webhook_type",
    "Labels": ".labels",
    "ParsedInventory": ".parsed_inventory",
    "ParsedInventorySourcesItem": ".parsed_inventory_sources_item",
    "ParsedInventorySourcesItemArguments": ".parsed_inventory_sources_item_arguments",
    "ParsedInventorySourcesItemArgumentsOneItem": ".parsed_inventory_sources_item_arguments_one_item",
    "SourceName": ".source_name",
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
    "CatalogCategory",
    "CatalogGroup",
    "CatalogName",
    "DataStatus",
    "EvidanceData",
    "Executable",
    "GetResponse",
    "IResolvedCatalog",
    "IResolvedSource",
    "IScan",
    "Insight",
    "IvcsInstalledApp",
    "IvcsInstalledAppType",
    "IvcsWebhook",
    "IvcsWebhookType",
    "Labels",
    "ParsedInventory",
    "ParsedInventorySourcesItem",
    "ParsedInventorySourcesItemArguments",
    "ParsedInventorySourcesItemArgumentsOneItem",
    "SourceName",
]
