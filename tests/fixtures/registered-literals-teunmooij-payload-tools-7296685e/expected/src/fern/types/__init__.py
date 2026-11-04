



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .access import Access
    from .access_collections_value import AccessCollectionsValue
    from .access_collections_value_create import AccessCollectionsValueCreate
    from .access_collections_value_delete import AccessCollectionsValueDelete
    from .access_collections_value_fields_value import AccessCollectionsValueFieldsValue
    from .access_collections_value_fields_value_create import AccessCollectionsValueFieldsValueCreate
    from .access_collections_value_fields_value_read import AccessCollectionsValueFieldsValueRead
    from .access_collections_value_fields_value_update import AccessCollectionsValueFieldsValueUpdate
    from .access_collections_value_read import AccessCollectionsValueRead
    from .access_collections_value_update import AccessCollectionsValueUpdate
    from .confirmation import Confirmation
    from .error import Error
    from .error_errors_item import ErrorErrorsItem
    from .my_global import MyGlobal
    from .my_global_upsert_confirmation import MyGlobalUpsertConfirmation
    from .pages import Pages
    from .pages_upsert_confirmation import PagesUpsertConfirmation
    from .pagess import Pagess
    from .shared_meta import SharedMeta
    from .users import Users
    from .users_me import UsersMe
    from .users_upsert_confirmation import UsersUpsertConfirmation
    from .userss import Userss
    from .where import Where
_dynamic_imports: typing.Dict[str, str] = {
    "Access": ".access",
    "AccessCollectionsValue": ".access_collections_value",
    "AccessCollectionsValueCreate": ".access_collections_value_create",
    "AccessCollectionsValueDelete": ".access_collections_value_delete",
    "AccessCollectionsValueFieldsValue": ".access_collections_value_fields_value",
    "AccessCollectionsValueFieldsValueCreate": ".access_collections_value_fields_value_create",
    "AccessCollectionsValueFieldsValueRead": ".access_collections_value_fields_value_read",
    "AccessCollectionsValueFieldsValueUpdate": ".access_collections_value_fields_value_update",
    "AccessCollectionsValueRead": ".access_collections_value_read",
    "AccessCollectionsValueUpdate": ".access_collections_value_update",
    "Confirmation": ".confirmation",
    "Error": ".error",
    "ErrorErrorsItem": ".error_errors_item",
    "MyGlobal": ".my_global",
    "MyGlobalUpsertConfirmation": ".my_global_upsert_confirmation",
    "Pages": ".pages",
    "PagesUpsertConfirmation": ".pages_upsert_confirmation",
    "Pagess": ".pagess",
    "SharedMeta": ".shared_meta",
    "Users": ".users",
    "UsersMe": ".users_me",
    "UsersUpsertConfirmation": ".users_upsert_confirmation",
    "Userss": ".userss",
    "Where": ".where",
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
    "Confirmation",
    "Error",
    "ErrorErrorsItem",
    "MyGlobal",
    "MyGlobalUpsertConfirmation",
    "Pages",
    "PagesUpsertConfirmation",
    "Pagess",
    "SharedMeta",
    "Users",
    "UsersMe",
    "UsersUpsertConfirmation",
    "Userss",
    "Where",
]
