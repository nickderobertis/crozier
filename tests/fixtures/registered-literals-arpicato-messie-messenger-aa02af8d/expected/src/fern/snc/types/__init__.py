



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_dm_response import CreateDmResponse
    from .get_contacts_response import GetContactsResponse
    from .group_create_params_avatar import GroupCreateParamsAvatar
    from .group_create_params_disappear import GroupCreateParamsDisappear
    from .group_create_params_name import GroupCreateParamsName
    from .group_create_params_topic import GroupCreateParamsTopic
    from .search_users_response import SearchUsersResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateDmResponse": ".create_dm_response",
    "GetContactsResponse": ".get_contacts_response",
    "GroupCreateParamsAvatar": ".group_create_params_avatar",
    "GroupCreateParamsDisappear": ".group_create_params_disappear",
    "GroupCreateParamsName": ".group_create_params_name",
    "GroupCreateParamsTopic": ".group_create_params_topic",
    "SearchUsersResponse": ".search_users_response",
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
    "CreateDmResponse",
    "GetContactsResponse",
    "GroupCreateParamsAvatar",
    "GroupCreateParamsDisappear",
    "GroupCreateParamsName",
    "GroupCreateParamsTopic",
    "SearchUsersResponse",
]
