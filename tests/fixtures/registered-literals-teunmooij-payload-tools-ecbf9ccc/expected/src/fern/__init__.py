



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Access,
        AccessCollectionsValue,
        AccessCollectionsValueCreate,
        AccessCollectionsValueDelete,
        AccessCollectionsValueFieldsValue,
        AccessCollectionsValueFieldsValueCreate,
        AccessCollectionsValueFieldsValueRead,
        AccessCollectionsValueFieldsValueUpdate,
        AccessCollectionsValueRead,
        AccessCollectionsValueUpdate,
        Confirmation,
        Error,
        ErrorErrorsItem,
        MyGlobal,
        MyGlobalUpsertConfirmation,
        Pages,
        PagesUpsertConfirmation,
        Pagess,
        Users,
        UsersMe,
        UsersUpsertConfirmation,
        Userss,
        Where,
    )
    from .errors import BadRequestError, NotFoundError, UnauthorizedError
    from . import auth, custom, global_my_global, pages, users
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .pages import DeletePagesResponse, PatchPagesResponse
    from .users import DeleteUsersResponse, PatchUsersResponse
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "Access": ".types",
    "AccessCollectionsValue": ".types",
    "AccessCollectionsValueCreate": ".types",
    "AccessCollectionsValueDelete": ".types",
    "AccessCollectionsValueFieldsValue": ".types",
    "AccessCollectionsValueFieldsValueCreate": ".types",
    "AccessCollectionsValueFieldsValueRead": ".types",
    "AccessCollectionsValueFieldsValueUpdate": ".types",
    "AccessCollectionsValueRead": ".types",
    "AccessCollectionsValueUpdate": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "Confirmation": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DeletePagesResponse": ".pages",
    "DeleteUsersResponse": ".users",
    "Error": ".types",
    "ErrorErrorsItem": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "MyGlobal": ".types",
    "MyGlobalUpsertConfirmation": ".types",
    "NotFoundError": ".errors",
    "Pages": ".types",
    "PagesUpsertConfirmation": ".types",
    "Pagess": ".types",
    "PatchPagesResponse": ".pages",
    "PatchUsersResponse": ".users",
    "UnauthorizedError": ".errors",
    "Users": ".types",
    "UsersMe": ".types",
    "UsersUpsertConfirmation": ".types",
    "Userss": ".types",
    "Where": ".types",
    "__version__": ".version",
    "auth": ".auth",
    "custom": ".custom",
    "global_my_global": ".global_my_global",
    "pages": ".pages",
    "users": ".users",
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
    "Access",
    "AccessCollectionsValue",
    "AccessCollectionsValueCreate",
    "AccessCollectionsValueDelete",
    "AccessCollectionsValueFieldsValue",
    "AccessCollectionsValueFieldsValueCreate",
    "AccessCollectionsValueFieldsValueRead",
    "AccessCollectionsValueFieldsValueUpdate",
    "AccessCollectionsValueRead",
    "AccessCollectionsValueUpdate",
    "AsyncFernApi",
    "BadRequestError",
    "Confirmation",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DeletePagesResponse",
    "DeleteUsersResponse",
    "Error",
    "ErrorErrorsItem",
    "FernApi",
    "FernApiEnvironment",
    "MyGlobal",
    "MyGlobalUpsertConfirmation",
    "NotFoundError",
    "Pages",
    "PagesUpsertConfirmation",
    "Pagess",
    "PatchPagesResponse",
    "PatchUsersResponse",
    "UnauthorizedError",
    "Users",
    "UsersMe",
    "UsersUpsertConfirmation",
    "Userss",
    "Where",
    "__version__",
    "auth",
    "custom",
    "global_my_global",
    "pages",
    "users",
]
