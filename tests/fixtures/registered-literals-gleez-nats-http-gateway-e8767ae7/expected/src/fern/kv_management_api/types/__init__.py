



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .add_kv_store_request_storage import AddKvStoreRequestStorage
    from .add_kv_store_request_x_nats_kv_storage import AddKvStoreRequestXNatsKvStorage
    from .kv_store_info_response import KvStoreInfoResponse
    from .kv_store_watch_request_include import KvStoreWatchRequestInclude
    from .kv_store_watch_response import KvStoreWatchResponse
    from .kv_store_watch_response_operation import KvStoreWatchResponseOperation
_dynamic_imports: typing.Dict[str, str] = {
    "AddKvStoreRequestStorage": ".add_kv_store_request_storage",
    "AddKvStoreRequestXNatsKvStorage": ".add_kv_store_request_x_nats_kv_storage",
    "KvStoreInfoResponse": ".kv_store_info_response",
    "KvStoreWatchRequestInclude": ".kv_store_watch_request_include",
    "KvStoreWatchResponse": ".kv_store_watch_response",
    "KvStoreWatchResponseOperation": ".kv_store_watch_response_operation",
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
    "KvStoreInfoResponse",
    "KvStoreWatchRequestInclude",
    "KvStoreWatchResponse",
    "KvStoreWatchResponseOperation",
]
