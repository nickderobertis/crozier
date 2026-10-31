



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .user_create_response import UserCreateResponse
    from .user_create_response_result import UserCreateResponseResult
    from .user_create_response_result_data import UserCreateResponseResultData
    from .user_list_response import UserListResponse
    from .user_list_response_result import UserListResponseResult
    from .user_list_response_result_data_item import UserListResponseResultDataItem
_dynamic_imports: typing.Dict[str, str] = {
    "UserCreateResponse": ".user_create_response",
    "UserCreateResponseResult": ".user_create_response_result",
    "UserCreateResponseResultData": ".user_create_response_result_data",
    "UserListResponse": ".user_list_response",
    "UserListResponseResult": ".user_list_response_result",
    "UserListResponseResultDataItem": ".user_list_response_result_data_item",
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
    "UserCreateResponse",
    "UserCreateResponseResult",
    "UserCreateResponseResultData",
    "UserListResponse",
    "UserListResponseResult",
    "UserListResponseResultDataItem",
]
