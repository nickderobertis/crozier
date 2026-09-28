



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CatalogCategory,
        CatalogGroup,
        CatalogName,
        DataStatus,
        EvidanceData,
        Executable,
        GetResponse,
        IResolvedCatalog,
        IResolvedSource,
        IScan,
        Insight,
        IvcsInstalledApp,
        IvcsInstalledAppType,
        IvcsWebhook,
        IvcsWebhookType,
        Labels,
        ParsedInventory,
        ParsedInventorySourcesItem,
        ParsedInventorySourcesItemArguments,
        ParsedInventorySourcesItemArgumentsOneItem,
        SourceName,
    )
    from .errors import InternalServerError
    from . import technologies
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "CatalogCategory": ".types",
    "CatalogGroup": ".types",
    "CatalogName": ".types",
    "DataStatus": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "EvidanceData": ".types",
    "Executable": ".types",
    "FernApi": ".client",
    "GetResponse": ".types",
    "IResolvedCatalog": ".types",
    "IResolvedSource": ".types",
    "IScan": ".types",
    "Insight": ".types",
    "InternalServerError": ".errors",
    "IvcsInstalledApp": ".types",
    "IvcsInstalledAppType": ".types",
    "IvcsWebhook": ".types",
    "IvcsWebhookType": ".types",
    "Labels": ".types",
    "ParsedInventory": ".types",
    "ParsedInventorySourcesItem": ".types",
    "ParsedInventorySourcesItemArguments": ".types",
    "ParsedInventorySourcesItemArgumentsOneItem": ".types",
    "SourceName": ".types",
    "__version__": ".version",
    "technologies": ".technologies",
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
    "AsyncFernApi",
    "CatalogCategory",
    "CatalogGroup",
    "CatalogName",
    "DataStatus",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "EvidanceData",
    "Executable",
    "FernApi",
    "GetResponse",
    "IResolvedCatalog",
    "IResolvedSource",
    "IScan",
    "Insight",
    "InternalServerError",
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
    "__version__",
    "technologies",
]
