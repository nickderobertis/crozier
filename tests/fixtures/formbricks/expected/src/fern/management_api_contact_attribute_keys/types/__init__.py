



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_contact_attribute_key_response import CreateContactAttributeKeyResponse
    from .create_contact_attribute_key_response_type import CreateContactAttributeKeyResponseType
    from .delete_contact_attribute_key_response import DeleteContactAttributeKeyResponse
    from .delete_contact_attribute_key_response_type import DeleteContactAttributeKeyResponseType
    from .get_contact_attribute_key_response import GetContactAttributeKeyResponse
    from .get_contact_attribute_key_response_type import GetContactAttributeKeyResponseType
    from .get_contact_attribute_keys_request_filter_date_field import GetContactAttributeKeysRequestFilterDateField
    from .get_contact_attribute_keys_request_order import GetContactAttributeKeysRequestOrder
    from .get_contact_attribute_keys_request_sort_by import GetContactAttributeKeysRequestSortBy
    from .get_contact_attribute_keys_response import GetContactAttributeKeysResponse
    from .get_contact_attribute_keys_response_data_item import GetContactAttributeKeysResponseDataItem
    from .get_contact_attribute_keys_response_data_item_type import GetContactAttributeKeysResponseDataItemType
    from .get_contact_attribute_keys_response_meta import GetContactAttributeKeysResponseMeta
    from .update_contact_attribute_key_response import UpdateContactAttributeKeyResponse
    from .update_contact_attribute_key_response_type import UpdateContactAttributeKeyResponseType
_dynamic_imports: typing.Dict[str, str] = {
    "CreateContactAttributeKeyResponse": ".create_contact_attribute_key_response",
    "CreateContactAttributeKeyResponseType": ".create_contact_attribute_key_response_type",
    "DeleteContactAttributeKeyResponse": ".delete_contact_attribute_key_response",
    "DeleteContactAttributeKeyResponseType": ".delete_contact_attribute_key_response_type",
    "GetContactAttributeKeyResponse": ".get_contact_attribute_key_response",
    "GetContactAttributeKeyResponseType": ".get_contact_attribute_key_response_type",
    "GetContactAttributeKeysRequestFilterDateField": ".get_contact_attribute_keys_request_filter_date_field",
    "GetContactAttributeKeysRequestOrder": ".get_contact_attribute_keys_request_order",
    "GetContactAttributeKeysRequestSortBy": ".get_contact_attribute_keys_request_sort_by",
    "GetContactAttributeKeysResponse": ".get_contact_attribute_keys_response",
    "GetContactAttributeKeysResponseDataItem": ".get_contact_attribute_keys_response_data_item",
    "GetContactAttributeKeysResponseDataItemType": ".get_contact_attribute_keys_response_data_item_type",
    "GetContactAttributeKeysResponseMeta": ".get_contact_attribute_keys_response_meta",
    "UpdateContactAttributeKeyResponse": ".update_contact_attribute_key_response",
    "UpdateContactAttributeKeyResponseType": ".update_contact_attribute_key_response_type",
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
    "CreateContactAttributeKeyResponse",
    "CreateContactAttributeKeyResponseType",
    "DeleteContactAttributeKeyResponse",
    "DeleteContactAttributeKeyResponseType",
    "GetContactAttributeKeyResponse",
    "GetContactAttributeKeyResponseType",
    "GetContactAttributeKeysRequestFilterDateField",
    "GetContactAttributeKeysRequestOrder",
    "GetContactAttributeKeysRequestSortBy",
    "GetContactAttributeKeysResponse",
    "GetContactAttributeKeysResponseDataItem",
    "GetContactAttributeKeysResponseDataItemType",
    "GetContactAttributeKeysResponseMeta",
    "UpdateContactAttributeKeyResponse",
    "UpdateContactAttributeKeyResponseType",
]
