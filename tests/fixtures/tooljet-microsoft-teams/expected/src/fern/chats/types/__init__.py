



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_chat_request_chat_type import CreateChatRequestChatType
    from .create_chat_request_installed_apps_item import CreateChatRequestInstalledAppsItem
    from .create_chat_request_installed_apps_item_consented_permission_set import (
        CreateChatRequestInstalledAppsItemConsentedPermissionSet,
    )
    from .create_chat_request_installed_apps_item_consented_permission_set_resource_specific_permissions_item import (
        CreateChatRequestInstalledAppsItemConsentedPermissionSetResourceSpecificPermissionsItem,
    )
    from .get_chat_request_expand import GetChatRequestExpand
    from .list_chats_request_expand import ListChatsRequestExpand
    from .list_chats_response import ListChatsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateChatRequestChatType": ".create_chat_request_chat_type",
    "CreateChatRequestInstalledAppsItem": ".create_chat_request_installed_apps_item",
    "CreateChatRequestInstalledAppsItemConsentedPermissionSet": ".create_chat_request_installed_apps_item_consented_permission_set",
    "CreateChatRequestInstalledAppsItemConsentedPermissionSetResourceSpecificPermissionsItem": ".create_chat_request_installed_apps_item_consented_permission_set_resource_specific_permissions_item",
    "GetChatRequestExpand": ".get_chat_request_expand",
    "ListChatsRequestExpand": ".list_chats_request_expand",
    "ListChatsResponse": ".list_chats_response",
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
    "CreateChatRequestChatType",
    "CreateChatRequestInstalledAppsItem",
    "CreateChatRequestInstalledAppsItemConsentedPermissionSet",
    "CreateChatRequestInstalledAppsItemConsentedPermissionSetResourceSpecificPermissionsItem",
    "GetChatRequestExpand",
    "ListChatsRequestExpand",
    "ListChatsResponse",
]
