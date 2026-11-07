



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .checkout_create_request_purpose import CheckoutCreateRequestPurpose
    from .get_payment_methods_response import GetPaymentMethodsResponse
    from .get_payment_methods_response_available_payment_methods_item import (
        GetPaymentMethodsResponseAvailablePaymentMethodsItem,
    )
    from .process_checkout_payment_type import ProcessCheckoutPaymentType
    from .process_checkout_response import ProcessCheckoutResponse
    from .process_checkout_response_payment_instrument import ProcessCheckoutResponsePaymentInstrument
_dynamic_imports: typing.Dict[str, str] = {
    "CheckoutCreateRequestPurpose": ".checkout_create_request_purpose",
    "GetPaymentMethodsResponse": ".get_payment_methods_response",
    "GetPaymentMethodsResponseAvailablePaymentMethodsItem": ".get_payment_methods_response_available_payment_methods_item",
    "ProcessCheckoutPaymentType": ".process_checkout_payment_type",
    "ProcessCheckoutResponse": ".process_checkout_response",
    "ProcessCheckoutResponsePaymentInstrument": ".process_checkout_response_payment_instrument",
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
    "CheckoutCreateRequestPurpose",
    "GetPaymentMethodsResponse",
    "GetPaymentMethodsResponseAvailablePaymentMethodsItem",
    "ProcessCheckoutPaymentType",
    "ProcessCheckoutResponse",
    "ProcessCheckoutResponsePaymentInstrument",
]
