



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .user_index_response import UserIndexResponse
    from .user_invite_response import UserInviteResponse
    from .user_restore_response import UserRestoreResponse
    from .user_show_response import UserShowResponse
    from .user_update_own_profile_response import UserUpdateOwnProfileResponse
    from .user_update_response import UserUpdateResponse
_dynamic_imports: typing.Dict[str, str] = {
    "UserIndexResponse": ".user_index_response",
    "UserInviteResponse": ".user_invite_response",
    "UserRestoreResponse": ".user_restore_response",
    "UserShowResponse": ".user_show_response",
    "UserUpdateOwnProfileResponse": ".user_update_own_profile_response",
    "UserUpdateResponse": ".user_update_response",
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
    "UserIndexResponse",
    "UserInviteResponse",
    "UserRestoreResponse",
    "UserShowResponse",
    "UserUpdateOwnProfileResponse",
    "UserUpdateResponse",
]
