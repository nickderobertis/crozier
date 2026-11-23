



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .coat import Coat
    from .query_response import QueryResponse, QueryResponse_StoreQueryV1, QueryResponse_StoreStatusV1
    from .query_result import QueryResult
    from .query_status import QueryStatus
    from .query_status_status import QueryStatusStatus
    from .shirt import Shirt
    from .store_item import StoreItem
    from .store_item_wearable import StoreItemWearable, StoreItemWearable_Jacket, StoreItemWearable_TShirt
_dynamic_imports: typing.Dict[str, str] = {
    "Coat": ".coat",
    "QueryResponse": ".query_response",
    "QueryResponse_StoreQueryV1": ".query_response",
    "QueryResponse_StoreStatusV1": ".query_response",
    "QueryResult": ".query_result",
    "QueryStatus": ".query_status",
    "QueryStatusStatus": ".query_status_status",
    "Shirt": ".shirt",
    "StoreItem": ".store_item",
    "StoreItemWearable": ".store_item_wearable",
    "StoreItemWearable_Jacket": ".store_item_wearable",
    "StoreItemWearable_TShirt": ".store_item_wearable",
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
    "Coat",
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
]
