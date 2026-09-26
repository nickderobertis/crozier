



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PostV2VectordbIndexesCreateRequestIndexParamsItem,
        PostV2VectordbIndexesCreateRequestIndexParamsItemIndexConfig,
        PostV2VectordbIndexesCreateResponse,
        PostV2VectordbIndexesCreateResponseData,
        PostV2VectordbIndexesDescribeResponse,
        PostV2VectordbIndexesDescribeResponseDataItem,
        PostV2VectordbIndexesDropResponse,
        PostV2VectordbIndexesDropResponseData,
        PostV2VectordbIndexesListResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostV2VectordbIndexesCreateRequestIndexParamsItem": ".types",
    "PostV2VectordbIndexesCreateRequestIndexParamsItemIndexConfig": ".types",
    "PostV2VectordbIndexesCreateResponse": ".types",
    "PostV2VectordbIndexesCreateResponseData": ".types",
    "PostV2VectordbIndexesDescribeResponse": ".types",
    "PostV2VectordbIndexesDescribeResponseDataItem": ".types",
    "PostV2VectordbIndexesDropResponse": ".types",
    "PostV2VectordbIndexesDropResponseData": ".types",
    "PostV2VectordbIndexesListResponse": ".types",
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
