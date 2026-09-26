



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PostV1VectorDeleteRequestId,
        PostV1VectorDeleteResponse,
        PostV1VectorDeleteResponseData,
        PostV1VectorDeleteResponseDataData,
        PostV1VectorDeleteResponseMessage,
        PostV1VectorGetRequestId,
        PostV1VectorGetResponse,
        PostV1VectorGetResponseData,
        PostV1VectorGetResponseDataDataItem,
        PostV1VectorGetResponseMessage,
        PostV1VectorInsertRequestData,
        PostV1VectorInsertRequestDataOneItem,
        PostV1VectorInsertRequestDataZero,
        PostV1VectorInsertResponse,
        PostV1VectorInsertResponseData,
        PostV1VectorInsertResponseDataData,
        PostV1VectorInsertResponseMessage,
        PostV1VectorQueryResponse,
        PostV1VectorQueryResponseData,
        PostV1VectorQueryResponseDataDataItem,
        PostV1VectorQueryResponseMessage,
        PostV1VectorSearchRequestParams,
        PostV1VectorSearchResponse,
        PostV1VectorSearchResponseData,
        PostV1VectorSearchResponseDataDataItem,
        PostV1VectorSearchResponseMessage,
        PostV1VectorUpsertRequestData,
        PostV1VectorUpsertRequestDataOneItem,
        PostV1VectorUpsertRequestDataZero,
        PostV1VectorUpsertResponse,
        PostV1VectorUpsertResponseData,
        PostV1VectorUpsertResponseDataData,
        PostV1VectorUpsertResponseMessage,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostV1VectorDeleteRequestId": ".types",
    "PostV1VectorDeleteResponse": ".types",
    "PostV1VectorDeleteResponseData": ".types",
    "PostV1VectorDeleteResponseDataData": ".types",
    "PostV1VectorDeleteResponseMessage": ".types",
    "PostV1VectorGetRequestId": ".types",
    "PostV1VectorGetResponse": ".types",
    "PostV1VectorGetResponseData": ".types",
    "PostV1VectorGetResponseDataDataItem": ".types",
    "PostV1VectorGetResponseMessage": ".types",
    "PostV1VectorInsertRequestData": ".types",
    "PostV1VectorInsertRequestDataOneItem": ".types",
    "PostV1VectorInsertRequestDataZero": ".types",
    "PostV1VectorInsertResponse": ".types",
    "PostV1VectorInsertResponseData": ".types",
    "PostV1VectorInsertResponseDataData": ".types",
    "PostV1VectorInsertResponseMessage": ".types",
    "PostV1VectorQueryResponse": ".types",
    "PostV1VectorQueryResponseData": ".types",
    "PostV1VectorQueryResponseDataDataItem": ".types",
    "PostV1VectorQueryResponseMessage": ".types",
    "PostV1VectorSearchRequestParams": ".types",
    "PostV1VectorSearchResponse": ".types",
    "PostV1VectorSearchResponseData": ".types",
    "PostV1VectorSearchResponseDataDataItem": ".types",
    "PostV1VectorSearchResponseMessage": ".types",
    "PostV1VectorUpsertRequestData": ".types",
    "PostV1VectorUpsertRequestDataOneItem": ".types",
    "PostV1VectorUpsertRequestDataZero": ".types",
    "PostV1VectorUpsertResponse": ".types",
    "PostV1VectorUpsertResponseData": ".types",
    "PostV1VectorUpsertResponseDataData": ".types",
    "PostV1VectorUpsertResponseMessage": ".types",
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
