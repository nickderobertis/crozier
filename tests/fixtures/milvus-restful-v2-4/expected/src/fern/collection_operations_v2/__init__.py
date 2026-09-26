



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PostV2VectordbCollectionsCreateRequestIndexParamsItem,
        PostV2VectordbCollectionsCreateRequestIndexParamsItemIndexConfig,
        PostV2VectordbCollectionsCreateRequestParams,
        PostV2VectordbCollectionsCreateRequestSchema,
        PostV2VectordbCollectionsCreateRequestSchemaFieldsItem,
        PostV2VectordbCollectionsCreateRequestSchemaFieldsItemElementTypeParams,
        PostV2VectordbCollectionsCreateResponse,
        PostV2VectordbCollectionsCreateResponseData,
        PostV2VectordbCollectionsDescribeResponse,
        PostV2VectordbCollectionsDescribeResponseData,
        PostV2VectordbCollectionsDescribeResponseDataFieldsItem,
        PostV2VectordbCollectionsDescribeResponseDataIndexesItem,
        PostV2VectordbCollectionsDropResponse,
        PostV2VectordbCollectionsDropResponseData,
        PostV2VectordbCollectionsGetLoadStateResponse,
        PostV2VectordbCollectionsGetLoadStateResponseData,
        PostV2VectordbCollectionsGetStatsResponse,
        PostV2VectordbCollectionsGetStatsResponseData,
        PostV2VectordbCollectionsHasResponse,
        PostV2VectordbCollectionsHasResponseData,
        PostV2VectordbCollectionsListResponse,
        PostV2VectordbCollectionsLoadResponse,
        PostV2VectordbCollectionsLoadResponseData,
        PostV2VectordbCollectionsReleaseResponse,
        PostV2VectordbCollectionsRenameResponse,
        PostV2VectordbCollectionsRenameResponseData,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostV2VectordbCollectionsCreateRequestIndexParamsItem": ".types",
    "PostV2VectordbCollectionsCreateRequestIndexParamsItemIndexConfig": ".types",
    "PostV2VectordbCollectionsCreateRequestParams": ".types",
    "PostV2VectordbCollectionsCreateRequestSchema": ".types",
    "PostV2VectordbCollectionsCreateRequestSchemaFieldsItem": ".types",
    "PostV2VectordbCollectionsCreateRequestSchemaFieldsItemElementTypeParams": ".types",
    "PostV2VectordbCollectionsCreateResponse": ".types",
    "PostV2VectordbCollectionsCreateResponseData": ".types",
    "PostV2VectordbCollectionsDescribeResponse": ".types",
    "PostV2VectordbCollectionsDescribeResponseData": ".types",
    "PostV2VectordbCollectionsDescribeResponseDataFieldsItem": ".types",
    "PostV2VectordbCollectionsDescribeResponseDataIndexesItem": ".types",
    "PostV2VectordbCollectionsDropResponse": ".types",
    "PostV2VectordbCollectionsDropResponseData": ".types",
    "PostV2VectordbCollectionsGetLoadStateResponse": ".types",
    "PostV2VectordbCollectionsGetLoadStateResponseData": ".types",
    "PostV2VectordbCollectionsGetStatsResponse": ".types",
    "PostV2VectordbCollectionsGetStatsResponseData": ".types",
    "PostV2VectordbCollectionsHasResponse": ".types",
    "PostV2VectordbCollectionsHasResponseData": ".types",
    "PostV2VectordbCollectionsListResponse": ".types",
    "PostV2VectordbCollectionsLoadResponse": ".types",
    "PostV2VectordbCollectionsLoadResponseData": ".types",
    "PostV2VectordbCollectionsReleaseResponse": ".types",
    "PostV2VectordbCollectionsRenameResponse": ".types",
    "PostV2VectordbCollectionsRenameResponseData": ".types",
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
