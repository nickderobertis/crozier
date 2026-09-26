



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from . import vector_operations
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .vector_operations import (
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
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "PostV1VectorDeleteRequestId": ".vector_operations",
    "PostV1VectorDeleteResponse": ".vector_operations",
    "PostV1VectorDeleteResponseData": ".vector_operations",
    "PostV1VectorDeleteResponseDataData": ".vector_operations",
    "PostV1VectorDeleteResponseMessage": ".vector_operations",
    "PostV1VectorGetRequestId": ".vector_operations",
    "PostV1VectorGetResponse": ".vector_operations",
    "PostV1VectorGetResponseData": ".vector_operations",
    "PostV1VectorGetResponseDataDataItem": ".vector_operations",
    "PostV1VectorGetResponseMessage": ".vector_operations",
    "PostV1VectorInsertRequestData": ".vector_operations",
    "PostV1VectorInsertRequestDataOneItem": ".vector_operations",
    "PostV1VectorInsertRequestDataZero": ".vector_operations",
    "PostV1VectorInsertResponse": ".vector_operations",
    "PostV1VectorInsertResponseData": ".vector_operations",
    "PostV1VectorInsertResponseDataData": ".vector_operations",
    "PostV1VectorInsertResponseMessage": ".vector_operations",
    "PostV1VectorQueryResponse": ".vector_operations",
    "PostV1VectorQueryResponseData": ".vector_operations",
    "PostV1VectorQueryResponseDataDataItem": ".vector_operations",
    "PostV1VectorQueryResponseMessage": ".vector_operations",
    "PostV1VectorSearchRequestParams": ".vector_operations",
    "PostV1VectorSearchResponse": ".vector_operations",
    "PostV1VectorSearchResponseData": ".vector_operations",
    "PostV1VectorSearchResponseDataDataItem": ".vector_operations",
    "PostV1VectorSearchResponseMessage": ".vector_operations",
    "PostV1VectorUpsertRequestData": ".vector_operations",
    "PostV1VectorUpsertRequestDataOneItem": ".vector_operations",
    "PostV1VectorUpsertRequestDataZero": ".vector_operations",
    "PostV1VectorUpsertResponse": ".vector_operations",
    "PostV1VectorUpsertResponseData": ".vector_operations",
    "PostV1VectorUpsertResponseDataData": ".vector_operations",
    "PostV1VectorUpsertResponseMessage": ".vector_operations",
    "__version__": ".version",
    "vector_operations": ".vector_operations",
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
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
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
    "__version__",
    "vector_operations",
]
