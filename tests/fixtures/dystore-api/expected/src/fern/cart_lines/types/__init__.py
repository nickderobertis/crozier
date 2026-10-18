



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_cart_line_add_to_cart_request_data import CreateCartLineAddToCartRequestData
    from .create_cart_line_add_to_cart_request_data_attributes import CreateCartLineAddToCartRequestDataAttributes
    from .update_cart_line_update_quantity_request_data import UpdateCartLineUpdateQuantityRequestData
    from .update_cart_line_update_quantity_request_data_attributes import (
        UpdateCartLineUpdateQuantityRequestDataAttributes,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateCartLineAddToCartRequestData": ".create_cart_line_add_to_cart_request_data",
    "CreateCartLineAddToCartRequestDataAttributes": ".create_cart_line_add_to_cart_request_data_attributes",
    "UpdateCartLineUpdateQuantityRequestData": ".update_cart_line_update_quantity_request_data",
    "UpdateCartLineUpdateQuantityRequestDataAttributes": ".update_cart_line_update_quantity_request_data_attributes",
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
    "CreateCartLineAddToCartRequestData",
    "CreateCartLineAddToCartRequestDataAttributes",
    "UpdateCartLineUpdateQuantityRequestData",
    "UpdateCartLineUpdateQuantityRequestDataAttributes",
]
