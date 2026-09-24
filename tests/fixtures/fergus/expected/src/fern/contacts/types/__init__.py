



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_contact_payload_contact_type import CreateContactPayloadContactType
    from .get_contacts_request_filter_contact_type import GetContactsRequestFilterContactType
    from .get_contacts_request_sort_field import GetContactsRequestSortField
    from .get_contacts_request_sort_order import GetContactsRequestSortOrder
_dynamic_imports: typing.Dict[str, str] = {
    "CreateContactPayloadContactType": ".create_contact_payload_contact_type",
    "GetContactsRequestFilterContactType": ".get_contacts_request_filter_contact_type",
    "GetContactsRequestSortField": ".get_contacts_request_sort_field",
    "GetContactsRequestSortOrder": ".get_contacts_request_sort_order",
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
    "CreateContactPayloadContactType",
    "GetContactsRequestFilterContactType",
    "GetContactsRequestSortField",
    "GetContactsRequestSortOrder",
]
