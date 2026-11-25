



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Coat,
        QueryResponse,
        QueryResponse_StoreQueryV1,
        QueryResponse_StoreStatusV1,
        QueryResult,
        QueryStatus,
        QueryStatusStatus,
        Shirt,
        StoreItem,
        StoreItemWearable,
        StoreItemWearable_Jacket,
        StoreItemWearable_TShirt,
    )
    from . import items
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "Coat": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "QueryResponse": ".types",
    "QueryResponse_StoreQueryV1": ".types",
    "QueryResponse_StoreStatusV1": ".types",
    "QueryResult": ".types",
    "QueryStatus": ".types",
    "QueryStatusStatus": ".types",
    "Shirt": ".types",
    "StoreItem": ".types",
    "StoreItemWearable": ".types",
    "StoreItemWearable_Jacket": ".types",
    "StoreItemWearable_TShirt": ".types",
    "__version__": ".version",
    "items": ".items",
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
    "Coat",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "QueryResponse",
    "QueryResponse_StoreQueryV1",
    "QueryResponse_StoreStatusV1",
    "QueryResult",
    "QueryStatus",
    "QueryStatusStatus",
    "Shirt",
    "StoreItem",
    "StoreItemWearable",
    "StoreItemWearable_Jacket",
    "StoreItemWearable_TShirt",
    "__version__",
    "items",
]
