



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BranchesList2Response,
        FileContentUpdate2RequestType,
        FilesCreate2RequestBody,
        FilesCreate2RequestBodyOne,
        FilesCreate2RequestBodyOneType,
        FilesCreate2RequestBodyZero,
        FilesCreate2RequestBodyZeroType,
        ValEnvironmentVariableGroupsListResponse,
        ValEnvironmentVariableGroupsListResponseDataItem,
        ValEnvironmentVariablesListResponse,
        ValFilesGet2Response,
        ValsCreate2RequestPrivacy,
        ValsList2RequestPrivacy,
        ValsList2Response,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "BranchesList2Response": ".types",
    "FileContentUpdate2RequestType": ".types",
    "FilesCreate2RequestBody": ".types",
    "FilesCreate2RequestBodyOne": ".types",
    "FilesCreate2RequestBodyOneType": ".types",
    "FilesCreate2RequestBodyZero": ".types",
    "FilesCreate2RequestBodyZeroType": ".types",
    "ValEnvironmentVariableGroupsListResponse": ".types",
    "ValEnvironmentVariableGroupsListResponseDataItem": ".types",
    "ValEnvironmentVariablesListResponse": ".types",
    "ValFilesGet2Response": ".types",
    "ValsCreate2RequestPrivacy": ".types",
    "ValsList2RequestPrivacy": ".types",
    "ValsList2Response": ".types",
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
    "BranchesList2Response",
    "FileContentUpdate2RequestType",
    "FilesCreate2RequestBody",
    "FilesCreate2RequestBodyOne",
    "FilesCreate2RequestBodyOneType",
    "FilesCreate2RequestBodyZero",
    "FilesCreate2RequestBodyZeroType",
    "ValEnvironmentVariableGroupsListResponse",
    "ValEnvironmentVariableGroupsListResponseDataItem",
    "ValEnvironmentVariablesListResponse",
    "ValFilesGet2Response",
    "ValsCreate2RequestPrivacy",
    "ValsList2RequestPrivacy",
    "ValsList2Response",
]
