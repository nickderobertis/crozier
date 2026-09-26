



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_v2vectordb_users_create_response import PostV2VectordbUsersCreateResponse
    from .post_v2vectordb_users_create_response_data import PostV2VectordbUsersCreateResponseData
    from .post_v2vectordb_users_describe_response import PostV2VectordbUsersDescribeResponse
    from .post_v2vectordb_users_drop_response import PostV2VectordbUsersDropResponse
    from .post_v2vectordb_users_drop_response_data import PostV2VectordbUsersDropResponseData
    from .post_v2vectordb_users_grant_role_response import PostV2VectordbUsersGrantRoleResponse
    from .post_v2vectordb_users_grant_role_response_data import PostV2VectordbUsersGrantRoleResponseData
    from .post_v2vectordb_users_list_response import PostV2VectordbUsersListResponse
    from .post_v2vectordb_users_revoke_role_response import PostV2VectordbUsersRevokeRoleResponse
    from .post_v2vectordb_users_revoke_role_response_data import PostV2VectordbUsersRevokeRoleResponseData
    from .post_v2vectordb_users_update_password_response import PostV2VectordbUsersUpdatePasswordResponse
    from .post_v2vectordb_users_update_password_response_data import PostV2VectordbUsersUpdatePasswordResponseData
_dynamic_imports: typing.Dict[str, str] = {
    "PostV2VectordbUsersCreateResponse": ".post_v2vectordb_users_create_response",
    "PostV2VectordbUsersCreateResponseData": ".post_v2vectordb_users_create_response_data",
    "PostV2VectordbUsersDescribeResponse": ".post_v2vectordb_users_describe_response",
    "PostV2VectordbUsersDropResponse": ".post_v2vectordb_users_drop_response",
    "PostV2VectordbUsersDropResponseData": ".post_v2vectordb_users_drop_response_data",
    "PostV2VectordbUsersGrantRoleResponse": ".post_v2vectordb_users_grant_role_response",
    "PostV2VectordbUsersGrantRoleResponseData": ".post_v2vectordb_users_grant_role_response_data",
    "PostV2VectordbUsersListResponse": ".post_v2vectordb_users_list_response",
    "PostV2VectordbUsersRevokeRoleResponse": ".post_v2vectordb_users_revoke_role_response",
    "PostV2VectordbUsersRevokeRoleResponseData": ".post_v2vectordb_users_revoke_role_response_data",
    "PostV2VectordbUsersUpdatePasswordResponse": ".post_v2vectordb_users_update_password_response",
    "PostV2VectordbUsersUpdatePasswordResponseData": ".post_v2vectordb_users_update_password_response_data",
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
