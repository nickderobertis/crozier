



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_v2vectordb_entities_delete_response import PostV2VectordbEntitiesDeleteResponse
    from .post_v2vectordb_entities_delete_response_data import PostV2VectordbEntitiesDeleteResponseData
    from .post_v2vectordb_entities_get_request_id import PostV2VectordbEntitiesGetRequestId
    from .post_v2vectordb_entities_get_response import PostV2VectordbEntitiesGetResponse
    from .post_v2vectordb_entities_get_response_data_item import PostV2VectordbEntitiesGetResponseDataItem
    from .post_v2vectordb_entities_insert_request_data import PostV2VectordbEntitiesInsertRequestData
    from .post_v2vectordb_entities_insert_request_data_one_item import PostV2VectordbEntitiesInsertRequestDataOneItem
    from .post_v2vectordb_entities_insert_request_data_zero import PostV2VectordbEntitiesInsertRequestDataZero
    from .post_v2vectordb_entities_insert_response import PostV2VectordbEntitiesInsertResponse
    from .post_v2vectordb_entities_insert_response_data import PostV2VectordbEntitiesInsertResponseData
    from .post_v2vectordb_entities_query_response import PostV2VectordbEntitiesQueryResponse
    from .post_v2vectordb_entities_query_response_data_item import PostV2VectordbEntitiesQueryResponseDataItem
    from .post_v2vectordb_entities_search_request_search_params import PostV2VectordbEntitiesSearchRequestSearchParams
    from .post_v2vectordb_entities_search_request_vector_item_item import (
        PostV2VectordbEntitiesSearchRequestVectorItemItem,
    )
    from .post_v2vectordb_entities_search_response import PostV2VectordbEntitiesSearchResponse
    from .post_v2vectordb_entities_search_response_data_item import PostV2VectordbEntitiesSearchResponseDataItem
    from .post_v2vectordb_entities_upsert_request_data import PostV2VectordbEntitiesUpsertRequestData
    from .post_v2vectordb_entities_upsert_request_data_one_item import PostV2VectordbEntitiesUpsertRequestDataOneItem
    from .post_v2vectordb_entities_upsert_request_data_zero import PostV2VectordbEntitiesUpsertRequestDataZero
    from .post_v2vectordb_entities_upsert_response import PostV2VectordbEntitiesUpsertResponse
    from .post_v2vectordb_entities_upsert_response_data import PostV2VectordbEntitiesUpsertResponseData
_dynamic_imports: typing.Dict[str, str] = {
    "PostV2VectordbEntitiesDeleteResponse": ".post_v2vectordb_entities_delete_response",
    "PostV2VectordbEntitiesDeleteResponseData": ".post_v2vectordb_entities_delete_response_data",
    "PostV2VectordbEntitiesGetRequestId": ".post_v2vectordb_entities_get_request_id",
    "PostV2VectordbEntitiesGetResponse": ".post_v2vectordb_entities_get_response",
    "PostV2VectordbEntitiesGetResponseDataItem": ".post_v2vectordb_entities_get_response_data_item",
    "PostV2VectordbEntitiesInsertRequestData": ".post_v2vectordb_entities_insert_request_data",
    "PostV2VectordbEntitiesInsertRequestDataOneItem": ".post_v2vectordb_entities_insert_request_data_one_item",
    "PostV2VectordbEntitiesInsertRequestDataZero": ".post_v2vectordb_entities_insert_request_data_zero",
    "PostV2VectordbEntitiesInsertResponse": ".post_v2vectordb_entities_insert_response",
    "PostV2VectordbEntitiesInsertResponseData": ".post_v2vectordb_entities_insert_response_data",
    "PostV2VectordbEntitiesQueryResponse": ".post_v2vectordb_entities_query_response",
    "PostV2VectordbEntitiesQueryResponseDataItem": ".post_v2vectordb_entities_query_response_data_item",
    "PostV2VectordbEntitiesSearchRequestSearchParams": ".post_v2vectordb_entities_search_request_search_params",
    "PostV2VectordbEntitiesSearchRequestVectorItemItem": ".post_v2vectordb_entities_search_request_vector_item_item",
    "PostV2VectordbEntitiesSearchResponse": ".post_v2vectordb_entities_search_response",
    "PostV2VectordbEntitiesSearchResponseDataItem": ".post_v2vectordb_entities_search_response_data_item",
    "PostV2VectordbEntitiesUpsertRequestData": ".post_v2vectordb_entities_upsert_request_data",
    "PostV2VectordbEntitiesUpsertRequestDataOneItem": ".post_v2vectordb_entities_upsert_request_data_one_item",
    "PostV2VectordbEntitiesUpsertRequestDataZero": ".post_v2vectordb_entities_upsert_request_data_zero",
    "PostV2VectordbEntitiesUpsertResponse": ".post_v2vectordb_entities_upsert_response",
    "PostV2VectordbEntitiesUpsertResponseData": ".post_v2vectordb_entities_upsert_response_data",
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
    "PostV2VectordbEntitiesDeleteResponse",
    "PostV2VectordbEntitiesDeleteResponseData",
    "PostV2VectordbEntitiesGetRequestId",
    "PostV2VectordbEntitiesGetResponse",
    "PostV2VectordbEntitiesGetResponseDataItem",
    "PostV2VectordbEntitiesInsertRequestData",
    "PostV2VectordbEntitiesInsertRequestDataOneItem",
    "PostV2VectordbEntitiesInsertRequestDataZero",
    "PostV2VectordbEntitiesInsertResponse",
    "PostV2VectordbEntitiesInsertResponseData",
    "PostV2VectordbEntitiesQueryResponse",
    "PostV2VectordbEntitiesQueryResponseDataItem",
    "PostV2VectordbEntitiesSearchRequestSearchParams",
    "PostV2VectordbEntitiesSearchRequestVectorItemItem",
    "PostV2VectordbEntitiesSearchResponse",
    "PostV2VectordbEntitiesSearchResponseDataItem",
    "PostV2VectordbEntitiesUpsertRequestData",
    "PostV2VectordbEntitiesUpsertRequestDataOneItem",
    "PostV2VectordbEntitiesUpsertRequestDataZero",
    "PostV2VectordbEntitiesUpsertResponse",
    "PostV2VectordbEntitiesUpsertResponseData",
]
