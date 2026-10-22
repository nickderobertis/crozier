



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AppConfig,
        AppConfigIconSize,
        AppConfigLayout,
        AppConfigStartingView,
        Config,
        Error,
        FileList,
        Item,
        ItemFields,
        ItemFieldsTarget,
        ItemResult,
        KeyValue,
        Page,
        PageInfo,
        Section,
        SectionFields,
        SectionResult,
        WriteResult,
    )
    from .errors import (
        BadRequestError,
        ContentTooLargeError,
        ForbiddenError,
        InternalServerError,
        NotFoundError,
        UnauthorizedError,
    )
    from . import files, items, keys, sections
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .items import UpdateItemResponse
    from .keys import GetConfigKeyRequestKey, ReplaceConfigKeyRequestKey
    from .sections import UpdateSectionResponse
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AppConfig": ".types",
    "AppConfigIconSize": ".types",
    "AppConfigLayout": ".types",
    "AppConfigStartingView": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "Config": ".types",
    "ContentTooLargeError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Error": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "FileList": ".types",
    "ForbiddenError": ".errors",
    "GetConfigKeyRequestKey": ".keys",
    "InternalServerError": ".errors",
    "Item": ".types",
    "ItemFields": ".types",
    "ItemFieldsTarget": ".types",
    "ItemResult": ".types",
    "KeyValue": ".types",
    "NotFoundError": ".errors",
    "Page": ".types",
    "PageInfo": ".types",
    "ReplaceConfigKeyRequestKey": ".keys",
    "Section": ".types",
    "SectionFields": ".types",
    "SectionResult": ".types",
    "UnauthorizedError": ".errors",
    "UpdateItemResponse": ".items",
    "UpdateSectionResponse": ".sections",
    "WriteResult": ".types",
    "__version__": ".version",
    "files": ".files",
    "items": ".items",
    "keys": ".keys",
    "sections": ".sections",
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
    "AppConfig",
    "AppConfigIconSize",
    "AppConfigLayout",
    "AppConfigStartingView",
    "AsyncFernApi",
    "BadRequestError",
    "Config",
    "ContentTooLargeError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Error",
    "FernApi",
    "FernApiEnvironment",
    "FileList",
    "ForbiddenError",
    "GetConfigKeyRequestKey",
    "InternalServerError",
    "Item",
    "ItemFields",
    "ItemFieldsTarget",
    "ItemResult",
    "KeyValue",
    "NotFoundError",
    "Page",
    "PageInfo",
    "ReplaceConfigKeyRequestKey",
    "Section",
    "SectionFields",
    "SectionResult",
    "UnauthorizedError",
    "UpdateItemResponse",
    "UpdateSectionResponse",
    "WriteResult",
    "__version__",
    "files",
    "items",
    "keys",
    "sections",
]
