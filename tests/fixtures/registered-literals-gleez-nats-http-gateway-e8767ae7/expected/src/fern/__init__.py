



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BadRequestErrorBody,
        Bucket,
        BucketConfig,
        BucketConfigStorage,
        Error,
        Header,
        Metadata,
        Msg,
        ObjectInfo,
        ObjectInfoLink,
        ObjectLink,
        Unknown,
        Value,
        ValueEvent,
        ValueEventOperation,
        ValueOperation,
    )
    from .errors import BadRequestError, ConflictError, NotFoundError
    from . import (
        extended_kv_entry_operations,
        kv_api,
        kv_management_api,
        nats_core_messaging_experimental,
        object_store_api,
        object_store_entry_operations,
        object_store_management_api,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .kv_management_api import (
        AddKvStoreRequestStorage,
        AddKvStoreRequestXNatsKvStorage,
        KvStoreInfoResponse,
        KvStoreWatchRequestInclude,
        KvStoreWatchResponse,
        KvStoreWatchResponseOperation,
    )
    from .nats_core_messaging_experimental import RequestResponse, SubscribeResponse
    from .object_store_entry_operations import ObjCreateEntryResponse, ObjCreateEntryResponseLink
    from .object_store_management_api import (
        ObjStoreWatchRequestInclude,
        ObjStoreWatchResponse,
        ObjStoreWatchResponseLink,
        ObjmStoreAddRequestStorage,
        ObjmStoreInfoResponse,
    )
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AddKvStoreRequestStorage": ".kv_management_api",
    "AddKvStoreRequestXNatsKvStorage": ".kv_management_api",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "BadRequestErrorBody": ".types",
    "Bucket": ".types",
    "BucketConfig": ".types",
    "BucketConfigStorage": ".types",
    "ConflictError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Error": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "Header": ".types",
    "KvStoreInfoResponse": ".kv_management_api",
    "KvStoreWatchRequestInclude": ".kv_management_api",
    "KvStoreWatchResponse": ".kv_management_api",
    "KvStoreWatchResponseOperation": ".kv_management_api",
    "Metadata": ".types",
    "Msg": ".types",
    "NotFoundError": ".errors",
    "ObjCreateEntryResponse": ".object_store_entry_operations",
    "ObjCreateEntryResponseLink": ".object_store_entry_operations",
    "ObjStoreWatchRequestInclude": ".object_store_management_api",
    "ObjStoreWatchResponse": ".object_store_management_api",
    "ObjStoreWatchResponseLink": ".object_store_management_api",
    "ObjectInfo": ".types",
    "ObjectInfoLink": ".types",
    "ObjectLink": ".types",
    "ObjmStoreAddRequestStorage": ".object_store_management_api",
    "ObjmStoreInfoResponse": ".object_store_management_api",
    "RequestResponse": ".nats_core_messaging_experimental",
    "SubscribeResponse": ".nats_core_messaging_experimental",
    "Unknown": ".types",
    "Value": ".types",
    "ValueEvent": ".types",
    "ValueEventOperation": ".types",
    "ValueOperation": ".types",
    "__version__": ".version",
    "extended_kv_entry_operations": ".extended_kv_entry_operations",
    "kv_api": ".kv_api",
    "kv_management_api": ".kv_management_api",
    "nats_core_messaging_experimental": ".nats_core_messaging_experimental",
    "object_store_api": ".object_store_api",
    "object_store_entry_operations": ".object_store_entry_operations",
    "object_store_management_api": ".object_store_management_api",
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
    "AddKvStoreRequestStorage",
    "AddKvStoreRequestXNatsKvStorage",
    "AsyncFernApi",
    "BadRequestError",
    "BadRequestErrorBody",
    "Bucket",
    "BucketConfig",
    "BucketConfigStorage",
    "ConflictError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Error",
    "FernApi",
    "FernApiEnvironment",
    "Header",
    "KvStoreInfoResponse",
    "KvStoreWatchRequestInclude",
    "KvStoreWatchResponse",
    "KvStoreWatchResponseOperation",
    "Metadata",
    "Msg",
    "NotFoundError",
    "ObjCreateEntryResponse",
    "ObjCreateEntryResponseLink",
    "ObjStoreWatchRequestInclude",
    "ObjStoreWatchResponse",
    "ObjStoreWatchResponseLink",
    "ObjectInfo",
    "ObjectInfoLink",
    "ObjectLink",
    "ObjmStoreAddRequestStorage",
    "ObjmStoreInfoResponse",
    "RequestResponse",
    "SubscribeResponse",
    "Unknown",
    "Value",
    "ValueEvent",
    "ValueEventOperation",
    "ValueOperation",
    "__version__",
    "extended_kv_entry_operations",
    "kv_api",
    "kv_management_api",
    "nats_core_messaging_experimental",
    "object_store_api",
    "object_store_entry_operations",
    "object_store_management_api",
]
