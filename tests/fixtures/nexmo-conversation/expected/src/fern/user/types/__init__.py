



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_user_response import CreateUserResponse
    from .get_user_response import GetUserResponse
    from .get_users_response_item import GetUsersResponseItem
    from .getuser_conversations_response_item import GetuserConversationsResponseItem
    from .getuser_conversations_response_item_timestamp import GetuserConversationsResponseItemTimestamp
    from .update_user_response import UpdateUserResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateUserResponse": ".create_user_response",
    "GetUserResponse": ".get_user_response",
    "GetUsersResponseItem": ".get_users_response_item",
    "GetuserConversationsResponseItem": ".getuser_conversations_response_item",
    "GetuserConversationsResponseItemTimestamp": ".getuser_conversations_response_item_timestamp",
    "UpdateUserResponse": ".update_user_response",
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
    "CreateUserResponse",
    "GetUserResponse",
    "GetUsersResponseItem",
    "GetuserConversationsResponseItem",
    "GetuserConversationsResponseItemTimestamp",
    "UpdateUserResponse",
]
