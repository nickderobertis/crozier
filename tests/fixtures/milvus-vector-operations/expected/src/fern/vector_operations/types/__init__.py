



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_v1vector_delete_request_id import PostV1VectorDeleteRequestId
    from .post_v1vector_delete_response import PostV1VectorDeleteResponse
    from .post_v1vector_delete_response_data import PostV1VectorDeleteResponseData
    from .post_v1vector_delete_response_data_data import PostV1VectorDeleteResponseDataData
    from .post_v1vector_delete_response_message import PostV1VectorDeleteResponseMessage
    from .post_v1vector_get_request_id import PostV1VectorGetRequestId
    from .post_v1vector_get_response import PostV1VectorGetResponse
    from .post_v1vector_get_response_data import PostV1VectorGetResponseData
    from .post_v1vector_get_response_data_data_item import PostV1VectorGetResponseDataDataItem
    from .post_v1vector_get_response_message import PostV1VectorGetResponseMessage
    from .post_v1vector_insert_request_data import PostV1VectorInsertRequestData
    from .post_v1vector_insert_request_data_one_item import PostV1VectorInsertRequestDataOneItem
    from .post_v1vector_insert_request_data_zero import PostV1VectorInsertRequestDataZero
    from .post_v1vector_insert_response import PostV1VectorInsertResponse
    from .post_v1vector_insert_response_data import PostV1VectorInsertResponseData
    from .post_v1vector_insert_response_data_data import PostV1VectorInsertResponseDataData
    from .post_v1vector_insert_response_message import PostV1VectorInsertResponseMessage
    from .post_v1vector_query_response import PostV1VectorQueryResponse
    from .post_v1vector_query_response_data import PostV1VectorQueryResponseData
    from .post_v1vector_query_response_data_data_item import PostV1VectorQueryResponseDataDataItem
    from .post_v1vector_query_response_message import PostV1VectorQueryResponseMessage
    from .post_v1vector_search_request_params import PostV1VectorSearchRequestParams
    from .post_v1vector_search_response import PostV1VectorSearchResponse
    from .post_v1vector_search_response_data import PostV1VectorSearchResponseData
    from .post_v1vector_search_response_data_data_item import PostV1VectorSearchResponseDataDataItem
    from .post_v1vector_search_response_message import PostV1VectorSearchResponseMessage
    from .post_v1vector_upsert_request_data import PostV1VectorUpsertRequestData
    from .post_v1vector_upsert_request_data_one_item import PostV1VectorUpsertRequestDataOneItem
    from .post_v1vector_upsert_request_data_zero import PostV1VectorUpsertRequestDataZero
    from .post_v1vector_upsert_response import PostV1VectorUpsertResponse
    from .post_v1vector_upsert_response_data import PostV1VectorUpsertResponseData
    from .post_v1vector_upsert_response_data_data import PostV1VectorUpsertResponseDataData
    from .post_v1vector_upsert_response_message import PostV1VectorUpsertResponseMessage
_dynamic_imports: typing.Dict[str, str] = {
    "PostV1VectorDeleteRequestId": ".post_v1vector_delete_request_id",
    "PostV1VectorDeleteResponse": ".post_v1vector_delete_response",
    "PostV1VectorDeleteResponseData": ".post_v1vector_delete_response_data",
    "PostV1VectorDeleteResponseDataData": ".post_v1vector_delete_response_data_data",
    "PostV1VectorDeleteResponseMessage": ".post_v1vector_delete_response_message",
    "PostV1VectorGetRequestId": ".post_v1vector_get_request_id",
    "PostV1VectorGetResponse": ".post_v1vector_get_response",
    "PostV1VectorGetResponseData": ".post_v1vector_get_response_data",
    "PostV1VectorGetResponseDataDataItem": ".post_v1vector_get_response_data_data_item",
    "PostV1VectorGetResponseMessage": ".post_v1vector_get_response_message",
    "PostV1VectorInsertRequestData": ".post_v1vector_insert_request_data",
    "PostV1VectorInsertRequestDataOneItem": ".post_v1vector_insert_request_data_one_item",
    "PostV1VectorInsertRequestDataZero": ".post_v1vector_insert_request_data_zero",
    "PostV1VectorInsertResponse": ".post_v1vector_insert_response",
    "PostV1VectorInsertResponseData": ".post_v1vector_insert_response_data",
    "PostV1VectorInsertResponseDataData": ".post_v1vector_insert_response_data_data",
    "PostV1VectorInsertResponseMessage": ".post_v1vector_insert_response_message",
    "PostV1VectorQueryResponse": ".post_v1vector_query_response",
    "PostV1VectorQueryResponseData": ".post_v1vector_query_response_data",
    "PostV1VectorQueryResponseDataDataItem": ".post_v1vector_query_response_data_data_item",
    "PostV1VectorQueryResponseMessage": ".post_v1vector_query_response_message",
    "PostV1VectorSearchRequestParams": ".post_v1vector_search_request_params",
    "PostV1VectorSearchResponse": ".post_v1vector_search_response",
    "PostV1VectorSearchResponseData": ".post_v1vector_search_response_data",
    "PostV1VectorSearchResponseDataDataItem": ".post_v1vector_search_response_data_data_item",
    "PostV1VectorSearchResponseMessage": ".post_v1vector_search_response_message",
    "PostV1VectorUpsertRequestData": ".post_v1vector_upsert_request_data",
    "PostV1VectorUpsertRequestDataOneItem": ".post_v1vector_upsert_request_data_one_item",
    "PostV1VectorUpsertRequestDataZero": ".post_v1vector_upsert_request_data_zero",
    "PostV1VectorUpsertResponse": ".post_v1vector_upsert_response",
    "PostV1VectorUpsertResponseData": ".post_v1vector_upsert_response_data",
    "PostV1VectorUpsertResponseDataData": ".post_v1vector_upsert_response_data_data",
    "PostV1VectorUpsertResponseMessage": ".post_v1vector_upsert_response_message",
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
    "PostV1VectorDeleteRequestId",
    "PostV1VectorDeleteResponse",
    "PostV1VectorDeleteResponseData",
    "PostV1VectorDeleteResponseDataData",
    "PostV1VectorDeleteResponseMessage",
    "PostV1VectorGetRequestId",
    "PostV1VectorGetResponse",
    "PostV1VectorGetResponseData",
    "PostV1VectorGetResponseDataDataItem",
    "PostV1VectorGetResponseMessage",
    "PostV1VectorInsertRequestData",
    "PostV1VectorInsertRequestDataOneItem",
    "PostV1VectorInsertRequestDataZero",
    "PostV1VectorInsertResponse",
    "PostV1VectorInsertResponseData",
    "PostV1VectorInsertResponseDataData",
    "PostV1VectorInsertResponseMessage",
    "PostV1VectorQueryResponse",
    "PostV1VectorQueryResponseData",
    "PostV1VectorQueryResponseDataDataItem",
    "PostV1VectorQueryResponseMessage",
    "PostV1VectorSearchRequestParams",
    "PostV1VectorSearchResponse",
    "PostV1VectorSearchResponseData",
    "PostV1VectorSearchResponseDataDataItem",
    "PostV1VectorSearchResponseMessage",
    "PostV1VectorUpsertRequestData",
    "PostV1VectorUpsertRequestDataOneItem",
    "PostV1VectorUpsertRequestDataZero",
    "PostV1VectorUpsertResponse",
    "PostV1VectorUpsertResponseData",
    "PostV1VectorUpsertResponseDataData",
    "PostV1VectorUpsertResponseMessage",
]
