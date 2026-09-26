



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .merchant_cart_calculate_response import MerchantCartCalculateResponse
    from .merchant_cert_create_request_customer_business_type import MerchantCertCreateRequestCustomerBusinessType
    from .merchant_cert_create_request_reason import MerchantCertCreateRequestReason
    from .merchant_cert_list_request_sort_by import MerchantCertListRequestSortBy
    from .merchant_order_create_from_cart_request_kind import MerchantOrderCreateFromCartRequestKind
    from .merchant_order_create_request_kind import MerchantOrderCreateRequestKind
    from .merchant_order_get_request_expand import MerchantOrderGetRequestExpand
_dynamic_imports: typing.Dict[str, str] = {
    "MerchantCartCalculateResponse": ".merchant_cart_calculate_response",
    "MerchantCertCreateRequestCustomerBusinessType": ".merchant_cert_create_request_customer_business_type",
    "MerchantCertCreateRequestReason": ".merchant_cert_create_request_reason",
    "MerchantCertListRequestSortBy": ".merchant_cert_list_request_sort_by",
    "MerchantOrderCreateFromCartRequestKind": ".merchant_order_create_from_cart_request_kind",
    "MerchantOrderCreateRequestKind": ".merchant_order_create_request_kind",
    "MerchantOrderGetRequestExpand": ".merchant_order_get_request_expand",
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
    "MerchantCartCalculateResponse",
    "MerchantCertCreateRequestCustomerBusinessType",
    "MerchantCertCreateRequestReason",
    "MerchantCertListRequestSortBy",
    "MerchantOrderCreateFromCartRequestKind",
    "MerchantOrderCreateRequestKind",
    "MerchantOrderGetRequestExpand",
]
