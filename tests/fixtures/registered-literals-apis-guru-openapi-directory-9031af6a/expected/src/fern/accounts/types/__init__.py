



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .add_user_to_account_request_account import AddUserToAccountRequestAccount
    from .add_user_to_account_request_users_item import AddUserToAccountRequestUsersItem
    from .add_user_to_account_request_users_item_identification import AddUserToAccountRequestUsersItemIdentification
    from .add_user_to_account_response import AddUserToAccountResponse
    from .add_user_to_account_response_meta import AddUserToAccountResponseMeta
    from .delete_account_request_identification import DeleteAccountRequestIdentification
    from .delete_account_response import DeleteAccountResponse
    from .delete_account_response_meta import DeleteAccountResponseMeta
    from .remove_user_from_account_request_account import RemoveUserFromAccountRequestAccount
    from .remove_user_from_account_request_users_item import RemoveUserFromAccountRequestUsersItem
    from .remove_user_from_account_request_users_item_identification import (
        RemoveUserFromAccountRequestUsersItemIdentification,
    )
    from .remove_user_from_account_response import RemoveUserFromAccountResponse
    from .remove_user_from_account_response_meta import RemoveUserFromAccountResponseMeta
    from .upsert_account_request_identification import UpsertAccountRequestIdentification
    from .upsert_account_request_properties_value import UpsertAccountRequestPropertiesValue
    from .upsert_account_response import UpsertAccountResponse
    from .upsert_account_response_meta import UpsertAccountResponseMeta
_dynamic_imports: typing.Dict[str, str] = {
    "AddUserToAccountRequestAccount": ".add_user_to_account_request_account",
    "AddUserToAccountRequestUsersItem": ".add_user_to_account_request_users_item",
    "AddUserToAccountRequestUsersItemIdentification": ".add_user_to_account_request_users_item_identification",
    "AddUserToAccountResponse": ".add_user_to_account_response",
    "AddUserToAccountResponseMeta": ".add_user_to_account_response_meta",
    "DeleteAccountRequestIdentification": ".delete_account_request_identification",
    "DeleteAccountResponse": ".delete_account_response",
    "DeleteAccountResponseMeta": ".delete_account_response_meta",
    "RemoveUserFromAccountRequestAccount": ".remove_user_from_account_request_account",
    "RemoveUserFromAccountRequestUsersItem": ".remove_user_from_account_request_users_item",
    "RemoveUserFromAccountRequestUsersItemIdentification": ".remove_user_from_account_request_users_item_identification",
    "RemoveUserFromAccountResponse": ".remove_user_from_account_response",
    "RemoveUserFromAccountResponseMeta": ".remove_user_from_account_response_meta",
    "UpsertAccountRequestIdentification": ".upsert_account_request_identification",
    "UpsertAccountRequestPropertiesValue": ".upsert_account_request_properties_value",
    "UpsertAccountResponse": ".upsert_account_response",
    "UpsertAccountResponseMeta": ".upsert_account_response_meta",
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
    "AddUserToAccountRequestAccount",
    "AddUserToAccountRequestUsersItem",
    "AddUserToAccountRequestUsersItemIdentification",
    "AddUserToAccountResponse",
    "AddUserToAccountResponseMeta",
    "DeleteAccountRequestIdentification",
    "DeleteAccountResponse",
    "DeleteAccountResponseMeta",
    "RemoveUserFromAccountRequestAccount",
    "RemoveUserFromAccountRequestUsersItem",
    "RemoveUserFromAccountRequestUsersItemIdentification",
    "RemoveUserFromAccountResponse",
    "RemoveUserFromAccountResponseMeta",
    "UpsertAccountRequestIdentification",
    "UpsertAccountRequestPropertiesValue",
    "UpsertAccountResponse",
    "UpsertAccountResponseMeta",
]
