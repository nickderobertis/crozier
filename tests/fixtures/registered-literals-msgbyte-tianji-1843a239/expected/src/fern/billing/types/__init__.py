



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .billing_credit_bills_response import BillingCreditBillsResponse
    from .billing_credit_bills_response_list_item import BillingCreditBillsResponseListItem
    from .billing_credit_checkout_response import BillingCreditCheckoutResponse
    from .billing_credit_packs_response_item import BillingCreditPacksResponseItem
    from .billing_credit_response import BillingCreditResponse
    from .billing_current_subscription_response import BillingCurrentSubscriptionResponse
    from .billing_current_tier_response import BillingCurrentTierResponse
    from .billing_limit_response import BillingLimitResponse
    from .billing_usage_response import BillingUsageResponse
_dynamic_imports: typing.Dict[str, str] = {
    "BillingCreditBillsResponse": ".billing_credit_bills_response",
    "BillingCreditBillsResponseListItem": ".billing_credit_bills_response_list_item",
    "BillingCreditCheckoutResponse": ".billing_credit_checkout_response",
    "BillingCreditPacksResponseItem": ".billing_credit_packs_response_item",
    "BillingCreditResponse": ".billing_credit_response",
    "BillingCurrentSubscriptionResponse": ".billing_current_subscription_response",
    "BillingCurrentTierResponse": ".billing_current_tier_response",
    "BillingLimitResponse": ".billing_limit_response",
    "BillingUsageResponse": ".billing_usage_response",
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
    "BillingCreditBillsResponse",
    "BillingCreditBillsResponseListItem",
    "BillingCreditCheckoutResponse",
    "BillingCreditPacksResponseItem",
    "BillingCreditResponse",
    "BillingCurrentSubscriptionResponse",
    "BillingCurrentTierResponse",
    "BillingLimitResponse",
    "BillingUsageResponse",
]
