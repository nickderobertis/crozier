



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PostV2VectordbAliasesAlterResponse,
        PostV2VectordbAliasesAlterResponseData,
        PostV2VectordbAliasesCreateResponse,
        PostV2VectordbAliasesCreateResponseData,
        PostV2VectordbAliasesDescribeResponse,
        PostV2VectordbAliasesDescribeResponseData,
        PostV2VectordbAliasesDropResponse,
        PostV2VectordbAliasesDropResponseData,
        PostV2VectordbAliasesListResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostV2VectordbAliasesAlterResponse": ".types",
    "PostV2VectordbAliasesAlterResponseData": ".types",
    "PostV2VectordbAliasesCreateResponse": ".types",
    "PostV2VectordbAliasesCreateResponseData": ".types",
    "PostV2VectordbAliasesDescribeResponse": ".types",
    "PostV2VectordbAliasesDescribeResponseData": ".types",
    "PostV2VectordbAliasesDropResponse": ".types",
    "PostV2VectordbAliasesDropResponseData": ".types",
    "PostV2VectordbAliasesListResponse": ".types",
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
    "PostV2VectordbAliasesAlterResponse",
    "PostV2VectordbAliasesAlterResponseData",
    "PostV2VectordbAliasesCreateResponse",
    "PostV2VectordbAliasesCreateResponseData",
    "PostV2VectordbAliasesDescribeResponse",
    "PostV2VectordbAliasesDescribeResponseData",
    "PostV2VectordbAliasesDropResponse",
    "PostV2VectordbAliasesDropResponseData",
    "PostV2VectordbAliasesListResponse",
]
