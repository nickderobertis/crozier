



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Address,
        BalanceTransaction,
        Customer,
        DataExport,
        EligibilityResponse,
        ErrorResponse,
        Order,
        Payment,
        PaymentPlanItem,
        Refund,
    )
    from .errors import BadRequestError, NotFoundError, UnauthorizedError
    from . import (
        addresses,
        balance_transactions,
        customers,
        data_exports,
        eligibility,
        orders,
        payments,
        refunds,
        webhooks,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .balance_transactions import ListbalancetransactionsResponse
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .payments import CreatePaymentRequestPayment, ListpaymentsResponse
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "BalanceTransaction": ".types",
    "CreatePaymentRequestPayment": ".payments",
    "Customer": ".types",
    "DataExport": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "EligibilityResponse": ".types",
    "ErrorResponse": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ListbalancetransactionsResponse": ".balance_transactions",
    "ListpaymentsResponse": ".payments",
    "NotFoundError": ".errors",
    "Order": ".types",
    "Payment": ".types",
    "PaymentPlanItem": ".types",
    "Refund": ".types",
    "UnauthorizedError": ".errors",
    "__version__": ".version",
    "addresses": ".addresses",
    "balance_transactions": ".balance_transactions",
    "customers": ".customers",
    "data_exports": ".data_exports",
    "eligibility": ".eligibility",
    "orders": ".orders",
    "payments": ".payments",
    "refunds": ".refunds",
    "webhooks": ".webhooks",
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
    "Address",
    "AsyncFernApi",
    "BadRequestError",
    "BalanceTransaction",
    "CreatePaymentRequestPayment",
    "Customer",
    "DataExport",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "EligibilityResponse",
    "ErrorResponse",
    "FernApi",
    "FernApiEnvironment",
    "ListbalancetransactionsResponse",
    "ListpaymentsResponse",
    "NotFoundError",
    "Order",
    "Payment",
    "PaymentPlanItem",
    "Refund",
    "UnauthorizedError",
    "__version__",
    "addresses",
    "balance_transactions",
    "customers",
    "data_exports",
    "eligibility",
    "orders",
    "payments",
    "refunds",
    "webhooks",
]
