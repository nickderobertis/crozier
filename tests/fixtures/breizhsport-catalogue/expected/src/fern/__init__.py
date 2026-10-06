



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import Article
    from . import catalogue, health
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .catalogue import (
        GetApiCatalogueResponse,
        PostApiCatalogueResponse,
        PutApiCatalogueQuantityResponse,
        PutApiCatalogueQuantityResponseArticlesItem,
        UpdateItemItemsItem,
    )
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .health import GetApiHealthResponse
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "Article": ".types",
    "AsyncFernApi": ".client",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetApiCatalogueResponse": ".catalogue",
    "GetApiHealthResponse": ".health",
    "PostApiCatalogueResponse": ".catalogue",
    "PutApiCatalogueQuantityResponse": ".catalogue",
    "PutApiCatalogueQuantityResponseArticlesItem": ".catalogue",
    "UpdateItemItemsItem": ".catalogue",
    "__version__": ".version",
    "catalogue": ".catalogue",
    "health": ".health",
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
    "Article",
    "AsyncFernApi",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "GetApiCatalogueResponse",
    "GetApiHealthResponse",
    "PostApiCatalogueResponse",
    "PutApiCatalogueQuantityResponse",
    "PutApiCatalogueQuantityResponseArticlesItem",
    "UpdateItemItemsItem",
    "__version__",
    "catalogue",
    "health",
]
