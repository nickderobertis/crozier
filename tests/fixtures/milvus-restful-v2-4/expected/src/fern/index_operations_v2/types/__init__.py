



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_v2vectordb_indexes_create_request_index_params_item import (
        PostV2VectordbIndexesCreateRequestIndexParamsItem,
    )
    from .post_v2vectordb_indexes_create_request_index_params_item_index_config import (
        PostV2VectordbIndexesCreateRequestIndexParamsItemIndexConfig,
    )
    from .post_v2vectordb_indexes_create_response import PostV2VectordbIndexesCreateResponse
    from .post_v2vectordb_indexes_create_response_data import PostV2VectordbIndexesCreateResponseData
    from .post_v2vectordb_indexes_describe_response import PostV2VectordbIndexesDescribeResponse
    from .post_v2vectordb_indexes_describe_response_data_item import PostV2VectordbIndexesDescribeResponseDataItem
    from .post_v2vectordb_indexes_drop_response import PostV2VectordbIndexesDropResponse
    from .post_v2vectordb_indexes_drop_response_data import PostV2VectordbIndexesDropResponseData
    from .post_v2vectordb_indexes_list_response import PostV2VectordbIndexesListResponse
_dynamic_imports: typing.Dict[str, str] = {
    "PostV2VectordbIndexesCreateRequestIndexParamsItem": ".post_v2vectordb_indexes_create_request_index_params_item",
    "PostV2VectordbIndexesCreateRequestIndexParamsItemIndexConfig": ".post_v2vectordb_indexes_create_request_index_params_item_index_config",
    "PostV2VectordbIndexesCreateResponse": ".post_v2vectordb_indexes_create_response",
    "PostV2VectordbIndexesCreateResponseData": ".post_v2vectordb_indexes_create_response_data",
    "PostV2VectordbIndexesDescribeResponse": ".post_v2vectordb_indexes_describe_response",
    "PostV2VectordbIndexesDescribeResponseDataItem": ".post_v2vectordb_indexes_describe_response_data_item",
    "PostV2VectordbIndexesDropResponse": ".post_v2vectordb_indexes_drop_response",
    "PostV2VectordbIndexesDropResponseData": ".post_v2vectordb_indexes_drop_response_data",
    "PostV2VectordbIndexesListResponse": ".post_v2vectordb_indexes_list_response",
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
    "PostV2VectordbIndexesCreateRequestIndexParamsItem",
    "PostV2VectordbIndexesCreateRequestIndexParamsItemIndexConfig",
    "PostV2VectordbIndexesCreateResponse",
    "PostV2VectordbIndexesCreateResponseData",
    "PostV2VectordbIndexesDescribeResponse",
    "PostV2VectordbIndexesDescribeResponseDataItem",
    "PostV2VectordbIndexesDropResponse",
    "PostV2VectordbIndexesDropResponseData",
    "PostV2VectordbIndexesListResponse",
]
