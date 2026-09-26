



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PostV2VectordbEntitiesDeleteResponse,
        PostV2VectordbEntitiesDeleteResponseData,
        PostV2VectordbEntitiesGetRequestId,
        PostV2VectordbEntitiesGetResponse,
        PostV2VectordbEntitiesGetResponseDataItem,
        PostV2VectordbEntitiesInsertRequestData,
        PostV2VectordbEntitiesInsertRequestDataOneItem,
        PostV2VectordbEntitiesInsertRequestDataZero,
        PostV2VectordbEntitiesInsertResponse,
        PostV2VectordbEntitiesInsertResponseData,
        PostV2VectordbEntitiesQueryResponse,
        PostV2VectordbEntitiesQueryResponseDataItem,
        PostV2VectordbEntitiesSearchRequestSearchParams,
        PostV2VectordbEntitiesSearchRequestVectorItemItem,
        PostV2VectordbEntitiesSearchResponse,
        PostV2VectordbEntitiesSearchResponseDataItem,
        PostV2VectordbEntitiesUpsertRequestData,
        PostV2VectordbEntitiesUpsertRequestDataOneItem,
        PostV2VectordbEntitiesUpsertRequestDataZero,
        PostV2VectordbEntitiesUpsertResponse,
        PostV2VectordbEntitiesUpsertResponseData,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostV2VectordbEntitiesDeleteResponse": ".types",
    "PostV2VectordbEntitiesDeleteResponseData": ".types",
    "PostV2VectordbEntitiesGetRequestId": ".types",
    "PostV2VectordbEntitiesGetResponse": ".types",
    "PostV2VectordbEntitiesGetResponseDataItem": ".types",
    "PostV2VectordbEntitiesInsertRequestData": ".types",
    "PostV2VectordbEntitiesInsertRequestDataOneItem": ".types",
    "PostV2VectordbEntitiesInsertRequestDataZero": ".types",
    "PostV2VectordbEntitiesInsertResponse": ".types",
    "PostV2VectordbEntitiesInsertResponseData": ".types",
    "PostV2VectordbEntitiesQueryResponse": ".types",
    "PostV2VectordbEntitiesQueryResponseDataItem": ".types",
    "PostV2VectordbEntitiesSearchRequestSearchParams": ".types",
    "PostV2VectordbEntitiesSearchRequestVectorItemItem": ".types",
    "PostV2VectordbEntitiesSearchResponse": ".types",
    "PostV2VectordbEntitiesSearchResponseDataItem": ".types",
    "PostV2VectordbEntitiesUpsertRequestData": ".types",
    "PostV2VectordbEntitiesUpsertRequestDataOneItem": ".types",
    "PostV2VectordbEntitiesUpsertRequestDataZero": ".types",
    "PostV2VectordbEntitiesUpsertResponse": ".types",
    "PostV2VectordbEntitiesUpsertResponseData": ".types",
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
