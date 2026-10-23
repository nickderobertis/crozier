



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_roles_response import GetRolesResponse
    from .get_roles_response_data_item import GetRolesResponseDataItem
    from .get_roles_response_data_item_one import GetRolesResponseDataItemOne
    from .get_roles_response_data_item_three import GetRolesResponseDataItemThree
    from .get_roles_response_data_item_two import GetRolesResponseDataItemTwo
    from .get_roles_response_data_item_zero import GetRolesResponseDataItemZero
_dynamic_imports: typing.Dict[str, str] = {
    "GetRolesResponse": ".get_roles_response",
    "GetRolesResponseDataItem": ".get_roles_response_data_item",
    "GetRolesResponseDataItemOne": ".get_roles_response_data_item_one",
    "GetRolesResponseDataItemThree": ".get_roles_response_data_item_three",
    "GetRolesResponseDataItemTwo": ".get_roles_response_data_item_two",
    "GetRolesResponseDataItemZero": ".get_roles_response_data_item_zero",
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
    "GetRolesResponse",
    "GetRolesResponseDataItem",
    "GetRolesResponseDataItemOne",
    "GetRolesResponseDataItemThree",
    "GetRolesResponseDataItemTwo",
    "GetRolesResponseDataItemZero",
]
