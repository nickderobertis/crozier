



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_v2vectordb_roles_create_response import PostV2VectordbRolesCreateResponse
    from .post_v2vectordb_roles_create_response_data import PostV2VectordbRolesCreateResponseData
    from .post_v2vectordb_roles_describe_response import PostV2VectordbRolesDescribeResponse
    from .post_v2vectordb_roles_describe_response_data_item import PostV2VectordbRolesDescribeResponseDataItem
    from .post_v2vectordb_roles_drop_response import PostV2VectordbRolesDropResponse
    from .post_v2vectordb_roles_drop_response_data import PostV2VectordbRolesDropResponseData
    from .post_v2vectordb_roles_grant_privilege_response import PostV2VectordbRolesGrantPrivilegeResponse
    from .post_v2vectordb_roles_grant_privilege_response_data import PostV2VectordbRolesGrantPrivilegeResponseData
    from .post_v2vectordb_roles_list_response import PostV2VectordbRolesListResponse
    from .post_v2vectordb_roles_revoke_privilege_response import PostV2VectordbRolesRevokePrivilegeResponse
    from .post_v2vectordb_roles_revoke_privilege_response_data import PostV2VectordbRolesRevokePrivilegeResponseData
_dynamic_imports: typing.Dict[str, str] = {
    "PostV2VectordbRolesCreateResponse": ".post_v2vectordb_roles_create_response",
    "PostV2VectordbRolesCreateResponseData": ".post_v2vectordb_roles_create_response_data",
    "PostV2VectordbRolesDescribeResponse": ".post_v2vectordb_roles_describe_response",
    "PostV2VectordbRolesDescribeResponseDataItem": ".post_v2vectordb_roles_describe_response_data_item",
    "PostV2VectordbRolesDropResponse": ".post_v2vectordb_roles_drop_response",
    "PostV2VectordbRolesDropResponseData": ".post_v2vectordb_roles_drop_response_data",
    "PostV2VectordbRolesGrantPrivilegeResponse": ".post_v2vectordb_roles_grant_privilege_response",
    "PostV2VectordbRolesGrantPrivilegeResponseData": ".post_v2vectordb_roles_grant_privilege_response_data",
    "PostV2VectordbRolesListResponse": ".post_v2vectordb_roles_list_response",
    "PostV2VectordbRolesRevokePrivilegeResponse": ".post_v2vectordb_roles_revoke_privilege_response",
    "PostV2VectordbRolesRevokePrivilegeResponseData": ".post_v2vectordb_roles_revoke_privilege_response_data",
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
    "PostV2VectordbRolesCreateResponse",
    "PostV2VectordbRolesCreateResponseData",
    "PostV2VectordbRolesDescribeResponse",
    "PostV2VectordbRolesDescribeResponseDataItem",
    "PostV2VectordbRolesDropResponse",
    "PostV2VectordbRolesDropResponseData",
    "PostV2VectordbRolesGrantPrivilegeResponse",
    "PostV2VectordbRolesGrantPrivilegeResponseData",
    "PostV2VectordbRolesListResponse",
    "PostV2VectordbRolesRevokePrivilegeResponse",
    "PostV2VectordbRolesRevokePrivilegeResponseData",
]
