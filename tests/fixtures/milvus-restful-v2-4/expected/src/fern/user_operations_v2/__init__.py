



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PostV2VectordbUsersCreateResponse,
        PostV2VectordbUsersCreateResponseData,
        PostV2VectordbUsersDescribeResponse,
        PostV2VectordbUsersDropResponse,
        PostV2VectordbUsersDropResponseData,
        PostV2VectordbUsersGrantRoleResponse,
        PostV2VectordbUsersGrantRoleResponseData,
        PostV2VectordbUsersListResponse,
        PostV2VectordbUsersRevokeRoleResponse,
        PostV2VectordbUsersRevokeRoleResponseData,
        PostV2VectordbUsersUpdatePasswordResponse,
        PostV2VectordbUsersUpdatePasswordResponseData,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostV2VectordbUsersCreateResponse": ".types",
    "PostV2VectordbUsersCreateResponseData": ".types",
    "PostV2VectordbUsersDescribeResponse": ".types",
    "PostV2VectordbUsersDropResponse": ".types",
    "PostV2VectordbUsersDropResponseData": ".types",
    "PostV2VectordbUsersGrantRoleResponse": ".types",
    "PostV2VectordbUsersGrantRoleResponseData": ".types",
    "PostV2VectordbUsersListResponse": ".types",
    "PostV2VectordbUsersRevokeRoleResponse": ".types",
    "PostV2VectordbUsersRevokeRoleResponseData": ".types",
    "PostV2VectordbUsersUpdatePasswordResponse": ".types",
    "PostV2VectordbUsersUpdatePasswordResponseData": ".types",
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
    "PostV2VectordbUsersCreateResponse",
    "PostV2VectordbUsersCreateResponseData",
    "PostV2VectordbUsersDescribeResponse",
    "PostV2VectordbUsersDropResponse",
    "PostV2VectordbUsersDropResponseData",
    "PostV2VectordbUsersGrantRoleResponse",
    "PostV2VectordbUsersGrantRoleResponseData",
    "PostV2VectordbUsersListResponse",
    "PostV2VectordbUsersRevokeRoleResponse",
    "PostV2VectordbUsersRevokeRoleResponseData",
    "PostV2VectordbUsersUpdatePasswordResponse",
    "PostV2VectordbUsersUpdatePasswordResponseData",
]
