



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_contact_response import CreateContactResponse
    from .upload_bulk_contacts_request_contacts_item import UploadBulkContactsRequestContactsItem
    from .upload_bulk_contacts_request_contacts_item_attributes_item import (
        UploadBulkContactsRequestContactsItemAttributesItem,
    )
    from .upload_bulk_contacts_request_contacts_item_attributes_item_attribute_key import (
        UploadBulkContactsRequestContactsItemAttributesItemAttributeKey,
    )
    from .upload_bulk_contacts_response import UploadBulkContactsResponse
    from .upload_bulk_contacts_response_data import UploadBulkContactsResponseData
_dynamic_imports: typing.Dict[str, str] = {
    "CreateContactResponse": ".create_contact_response",
    "UploadBulkContactsRequestContactsItem": ".upload_bulk_contacts_request_contacts_item",
    "UploadBulkContactsRequestContactsItemAttributesItem": ".upload_bulk_contacts_request_contacts_item_attributes_item",
    "UploadBulkContactsRequestContactsItemAttributesItemAttributeKey": ".upload_bulk_contacts_request_contacts_item_attributes_item_attribute_key",
    "UploadBulkContactsResponse": ".upload_bulk_contacts_response",
    "UploadBulkContactsResponseData": ".upload_bulk_contacts_response_data",
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
    "CreateContactResponse",
    "UploadBulkContactsRequestContactsItem",
    "UploadBulkContactsRequestContactsItemAttributesItem",
    "UploadBulkContactsRequestContactsItemAttributesItemAttributeKey",
    "UploadBulkContactsResponse",
    "UploadBulkContactsResponseData",
]
