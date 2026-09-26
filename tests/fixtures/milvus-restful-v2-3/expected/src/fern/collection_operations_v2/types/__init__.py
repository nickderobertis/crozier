



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_v2vectordb_collections_describe_response import PostV2VectordbCollectionsDescribeResponse
    from .post_v2vectordb_collections_describe_response_data import PostV2VectordbCollectionsDescribeResponseData
    from .post_v2vectordb_collections_describe_response_data_fields_item import (
        PostV2VectordbCollectionsDescribeResponseDataFieldsItem,
    )
    from .post_v2vectordb_collections_describe_response_data_indexes_item import (
        PostV2VectordbCollectionsDescribeResponseDataIndexesItem,
    )
    from .post_v2vectordb_collections_release_response import PostV2VectordbCollectionsReleaseResponse
_dynamic_imports: typing.Dict[str, str] = {
    "PostV2VectordbCollectionsDescribeResponse": ".post_v2vectordb_collections_describe_response",
    "PostV2VectordbCollectionsDescribeResponseData": ".post_v2vectordb_collections_describe_response_data",
    "PostV2VectordbCollectionsDescribeResponseDataFieldsItem": ".post_v2vectordb_collections_describe_response_data_fields_item",
    "PostV2VectordbCollectionsDescribeResponseDataIndexesItem": ".post_v2vectordb_collections_describe_response_data_indexes_item",
    "PostV2VectordbCollectionsReleaseResponse": ".post_v2vectordb_collections_release_response",
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
    "PostV2VectordbCollectionsDescribeResponse",
    "PostV2VectordbCollectionsDescribeResponseData",
    "PostV2VectordbCollectionsDescribeResponseDataFieldsItem",
    "PostV2VectordbCollectionsDescribeResponseDataIndexesItem",
    "PostV2VectordbCollectionsReleaseResponse",
]
