



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_account_properties_response import GetAccountPropertiesResponse
    from .get_account_properties_response_data_item import GetAccountPropertiesResponseDataItem
    from .get_account_properties_response_data_item_group import GetAccountPropertiesResponseDataItemGroup
    from .get_account_properties_response_meta import GetAccountPropertiesResponseMeta
    from .get_user_properties_response import GetUserPropertiesResponse
    from .get_user_properties_response_data_item import GetUserPropertiesResponseDataItem
    from .get_user_properties_response_data_item_group import GetUserPropertiesResponseDataItemGroup
    from .get_user_properties_response_meta import GetUserPropertiesResponseMeta
_dynamic_imports: typing.Dict[str, str] = {
    "GetAccountPropertiesResponse": ".get_account_properties_response",
    "GetAccountPropertiesResponseDataItem": ".get_account_properties_response_data_item",
    "GetAccountPropertiesResponseDataItemGroup": ".get_account_properties_response_data_item_group",
    "GetAccountPropertiesResponseMeta": ".get_account_properties_response_meta",
    "GetUserPropertiesResponse": ".get_user_properties_response",
    "GetUserPropertiesResponseDataItem": ".get_user_properties_response_data_item",
    "GetUserPropertiesResponseDataItemGroup": ".get_user_properties_response_data_item_group",
    "GetUserPropertiesResponseMeta": ".get_user_properties_response_meta",
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
    "GetAccountPropertiesResponse",
    "GetAccountPropertiesResponseDataItem",
    "GetAccountPropertiesResponseDataItemGroup",
    "GetAccountPropertiesResponseMeta",
    "GetUserPropertiesResponse",
    "GetUserPropertiesResponseDataItem",
    "GetUserPropertiesResponseDataItemGroup",
    "GetUserPropertiesResponseMeta",
]
