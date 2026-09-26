



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_v2vectordb_collections_create_request_index_params_item import (
        PostV2VectordbCollectionsCreateRequestIndexParamsItem,
    )
    from .post_v2vectordb_collections_create_request_index_params_item_index_config import (
        PostV2VectordbCollectionsCreateRequestIndexParamsItemIndexConfig,
    )
    from .post_v2vectordb_collections_create_request_params import PostV2VectordbCollectionsCreateRequestParams
    from .post_v2vectordb_collections_create_request_schema import PostV2VectordbCollectionsCreateRequestSchema
    from .post_v2vectordb_collections_create_request_schema_fields_item import (
        PostV2VectordbCollectionsCreateRequestSchemaFieldsItem,
    )
    from .post_v2vectordb_collections_create_request_schema_fields_item_element_type_params import (
        PostV2VectordbCollectionsCreateRequestSchemaFieldsItemElementTypeParams,
    )
    from .post_v2vectordb_collections_create_response import PostV2VectordbCollectionsCreateResponse
    from .post_v2vectordb_collections_create_response_data import PostV2VectordbCollectionsCreateResponseData
    from .post_v2vectordb_collections_describe_response import PostV2VectordbCollectionsDescribeResponse
    from .post_v2vectordb_collections_describe_response_data import PostV2VectordbCollectionsDescribeResponseData
    from .post_v2vectordb_collections_describe_response_data_fields_item import (
        PostV2VectordbCollectionsDescribeResponseDataFieldsItem,
    )
    from .post_v2vectordb_collections_describe_response_data_indexes_item import (
        PostV2VectordbCollectionsDescribeResponseDataIndexesItem,
    )
    from .post_v2vectordb_collections_drop_response import PostV2VectordbCollectionsDropResponse
    from .post_v2vectordb_collections_drop_response_data import PostV2VectordbCollectionsDropResponseData
    from .post_v2vectordb_collections_get_load_state_response import PostV2VectordbCollectionsGetLoadStateResponse
    from .post_v2vectordb_collections_get_load_state_response_data import (
        PostV2VectordbCollectionsGetLoadStateResponseData,
    )
    from .post_v2vectordb_collections_get_stats_response import PostV2VectordbCollectionsGetStatsResponse
    from .post_v2vectordb_collections_get_stats_response_data import PostV2VectordbCollectionsGetStatsResponseData
    from .post_v2vectordb_collections_has_response import PostV2VectordbCollectionsHasResponse
    from .post_v2vectordb_collections_has_response_data import PostV2VectordbCollectionsHasResponseData
    from .post_v2vectordb_collections_list_response import PostV2VectordbCollectionsListResponse
    from .post_v2vectordb_collections_load_response import PostV2VectordbCollectionsLoadResponse
    from .post_v2vectordb_collections_load_response_data import PostV2VectordbCollectionsLoadResponseData
    from .post_v2vectordb_collections_release_response import PostV2VectordbCollectionsReleaseResponse
    from .post_v2vectordb_collections_rename_response import PostV2VectordbCollectionsRenameResponse
    from .post_v2vectordb_collections_rename_response_data import PostV2VectordbCollectionsRenameResponseData
_dynamic_imports: typing.Dict[str, str] = {
    "PostV2VectordbCollectionsCreateRequestIndexParamsItem": ".post_v2vectordb_collections_create_request_index_params_item",
    "PostV2VectordbCollectionsCreateRequestIndexParamsItemIndexConfig": ".post_v2vectordb_collections_create_request_index_params_item_index_config",
    "PostV2VectordbCollectionsCreateRequestParams": ".post_v2vectordb_collections_create_request_params",
    "PostV2VectordbCollectionsCreateRequestSchema": ".post_v2vectordb_collections_create_request_schema",
    "PostV2VectordbCollectionsCreateRequestSchemaFieldsItem": ".post_v2vectordb_collections_create_request_schema_fields_item",
    "PostV2VectordbCollectionsCreateRequestSchemaFieldsItemElementTypeParams": ".post_v2vectordb_collections_create_request_schema_fields_item_element_type_params",
    "PostV2VectordbCollectionsCreateResponse": ".post_v2vectordb_collections_create_response",
    "PostV2VectordbCollectionsCreateResponseData": ".post_v2vectordb_collections_create_response_data",
    "PostV2VectordbCollectionsDescribeResponse": ".post_v2vectordb_collections_describe_response",
    "PostV2VectordbCollectionsDescribeResponseData": ".post_v2vectordb_collections_describe_response_data",
    "PostV2VectordbCollectionsDescribeResponseDataFieldsItem": ".post_v2vectordb_collections_describe_response_data_fields_item",
    "PostV2VectordbCollectionsDescribeResponseDataIndexesItem": ".post_v2vectordb_collections_describe_response_data_indexes_item",
    "PostV2VectordbCollectionsDropResponse": ".post_v2vectordb_collections_drop_response",
    "PostV2VectordbCollectionsDropResponseData": ".post_v2vectordb_collections_drop_response_data",
    "PostV2VectordbCollectionsGetLoadStateResponse": ".post_v2vectordb_collections_get_load_state_response",
    "PostV2VectordbCollectionsGetLoadStateResponseData": ".post_v2vectordb_collections_get_load_state_response_data",
    "PostV2VectordbCollectionsGetStatsResponse": ".post_v2vectordb_collections_get_stats_response",
    "PostV2VectordbCollectionsGetStatsResponseData": ".post_v2vectordb_collections_get_stats_response_data",
    "PostV2VectordbCollectionsHasResponse": ".post_v2vectordb_collections_has_response",
    "PostV2VectordbCollectionsHasResponseData": ".post_v2vectordb_collections_has_response_data",
    "PostV2VectordbCollectionsListResponse": ".post_v2vectordb_collections_list_response",
    "PostV2VectordbCollectionsLoadResponse": ".post_v2vectordb_collections_load_response",
    "PostV2VectordbCollectionsLoadResponseData": ".post_v2vectordb_collections_load_response_data",
    "PostV2VectordbCollectionsReleaseResponse": ".post_v2vectordb_collections_release_response",
    "PostV2VectordbCollectionsRenameResponse": ".post_v2vectordb_collections_rename_response",
    "PostV2VectordbCollectionsRenameResponseData": ".post_v2vectordb_collections_rename_response_data",
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
    "PostV2VectordbCollectionsCreateRequestIndexParamsItem",
    "PostV2VectordbCollectionsCreateRequestIndexParamsItemIndexConfig",
    "PostV2VectordbCollectionsCreateRequestParams",
    "PostV2VectordbCollectionsCreateRequestSchema",
    "PostV2VectordbCollectionsCreateRequestSchemaFieldsItem",
    "PostV2VectordbCollectionsCreateRequestSchemaFieldsItemElementTypeParams",
    "PostV2VectordbCollectionsCreateResponse",
    "PostV2VectordbCollectionsCreateResponseData",
    "PostV2VectordbCollectionsDescribeResponse",
    "PostV2VectordbCollectionsDescribeResponseData",
    "PostV2VectordbCollectionsDescribeResponseDataFieldsItem",
    "PostV2VectordbCollectionsDescribeResponseDataIndexesItem",
    "PostV2VectordbCollectionsDropResponse",
    "PostV2VectordbCollectionsDropResponseData",
    "PostV2VectordbCollectionsGetLoadStateResponse",
    "PostV2VectordbCollectionsGetLoadStateResponseData",
    "PostV2VectordbCollectionsGetStatsResponse",
    "PostV2VectordbCollectionsGetStatsResponseData",
    "PostV2VectordbCollectionsHasResponse",
    "PostV2VectordbCollectionsHasResponseData",
    "PostV2VectordbCollectionsListResponse",
    "PostV2VectordbCollectionsLoadResponse",
    "PostV2VectordbCollectionsLoadResponseData",
    "PostV2VectordbCollectionsReleaseResponse",
    "PostV2VectordbCollectionsRenameResponse",
    "PostV2VectordbCollectionsRenameResponseData",
]
