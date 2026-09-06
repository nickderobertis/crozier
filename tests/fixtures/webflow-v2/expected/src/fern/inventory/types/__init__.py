



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .ecomm_inventory_changed_payload import EcommInventoryChangedPayload
    from .ecomm_inventory_changed_payload_payload import EcommInventoryChangedPayloadPayload
    from .ecomm_inventory_changed_payload_payload_inventory_type import EcommInventoryChangedPayloadPayloadInventoryType
    from .ecomm_inventory_changed_payload_trigger_type import EcommInventoryChangedPayloadTriggerType
    from .list_inventory_response import ListInventoryResponse
    from .list_inventory_response_inventory_type import ListInventoryResponseInventoryType
    from .update_inventory_request_inventory_type import UpdateInventoryRequestInventoryType
    from .update_inventory_response import UpdateInventoryResponse
    from .update_inventory_response_inventory_type import UpdateInventoryResponseInventoryType
_dynamic_imports: typing.Dict[str, str] = {
    "EcommInventoryChangedPayload": ".ecomm_inventory_changed_payload",
    "EcommInventoryChangedPayloadPayload": ".ecomm_inventory_changed_payload_payload",
    "EcommInventoryChangedPayloadPayloadInventoryType": ".ecomm_inventory_changed_payload_payload_inventory_type",
    "EcommInventoryChangedPayloadTriggerType": ".ecomm_inventory_changed_payload_trigger_type",
    "ListInventoryResponse": ".list_inventory_response",
    "ListInventoryResponseInventoryType": ".list_inventory_response_inventory_type",
    "UpdateInventoryRequestInventoryType": ".update_inventory_request_inventory_type",
    "UpdateInventoryResponse": ".update_inventory_response",
    "UpdateInventoryResponseInventoryType": ".update_inventory_response_inventory_type",
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
    "EcommInventoryChangedPayload",
    "EcommInventoryChangedPayloadPayload",
    "EcommInventoryChangedPayloadPayloadInventoryType",
    "EcommInventoryChangedPayloadTriggerType",
    "ListInventoryResponse",
    "ListInventoryResponseInventoryType",
    "UpdateInventoryRequestInventoryType",
    "UpdateInventoryResponse",
    "UpdateInventoryResponseInventoryType",
]
