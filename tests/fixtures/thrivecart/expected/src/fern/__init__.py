



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import ApiError, Customer, EventSubscription, Product, ProductStatus, Transaction, TransactionType
    from .errors import BadRequestError, UnauthorizedError
    from . import coupons, customers, event_subscriptions, products, students, subscriptions, transactions, utilities
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .coupons import CreateCouponRequestDiscountType, CreateCouponResponse, ListCouponsResponse
    from .customers import GetCustomerResponse
    from .environment import FernApiEnvironment
    from .event_subscriptions import (
        CreateEventSubscriptionRequestEvent,
        CreateEventSubscriptionResponse,
        DeleteEventSubscriptionResponse,
    )
    from .products import GetProductResponse, ListProductsRequestStatus, ListProductsResponse
    from .students import CreateStudentResponse
    from .subscriptions import CancelSubscriptionResponse, PauseSubscriptionResponse, ResumeSubscriptionResponse
    from .transactions import GetTransactionResponse, ListTransactionsResponse, RefundTransactionResponse
    from .utilities import GetCustomerHubEmbedResponse, PingResponse
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "ApiError": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "CancelSubscriptionResponse": ".subscriptions",
    "CreateCouponRequestDiscountType": ".coupons",
    "CreateCouponResponse": ".coupons",
    "CreateEventSubscriptionRequestEvent": ".event_subscriptions",
    "CreateEventSubscriptionResponse": ".event_subscriptions",
    "CreateStudentResponse": ".students",
    "Customer": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DeleteEventSubscriptionResponse": ".event_subscriptions",
    "EventSubscription": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetCustomerHubEmbedResponse": ".utilities",
    "GetCustomerResponse": ".customers",
    "GetProductResponse": ".products",
    "GetTransactionResponse": ".transactions",
    "ListCouponsResponse": ".coupons",
    "ListProductsRequestStatus": ".products",
    "ListProductsResponse": ".products",
    "ListTransactionsResponse": ".transactions",
    "PauseSubscriptionResponse": ".subscriptions",
    "PingResponse": ".utilities",
    "Product": ".types",
    "ProductStatus": ".types",
    "RefundTransactionResponse": ".transactions",
    "ResumeSubscriptionResponse": ".subscriptions",
    "Transaction": ".types",
    "TransactionType": ".types",
    "UnauthorizedError": ".errors",
    "__version__": ".version",
    "coupons": ".coupons",
    "customers": ".customers",
    "event_subscriptions": ".event_subscriptions",
    "products": ".products",
    "students": ".students",
    "subscriptions": ".subscriptions",
    "transactions": ".transactions",
    "utilities": ".utilities",
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
    "ApiError",
    "AsyncFernApi",
    "BadRequestError",
    "CancelSubscriptionResponse",
    "CreateCouponRequestDiscountType",
    "CreateCouponResponse",
    "CreateEventSubscriptionRequestEvent",
    "CreateEventSubscriptionResponse",
    "CreateStudentResponse",
    "Customer",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DeleteEventSubscriptionResponse",
    "EventSubscription",
    "FernApi",
    "FernApiEnvironment",
    "GetCustomerHubEmbedResponse",
    "GetCustomerResponse",
    "GetProductResponse",
    "GetTransactionResponse",
    "ListCouponsResponse",
    "ListProductsRequestStatus",
    "ListProductsResponse",
    "ListTransactionsResponse",
    "PauseSubscriptionResponse",
    "PingResponse",
    "Product",
    "ProductStatus",
    "RefundTransactionResponse",
    "ResumeSubscriptionResponse",
    "Transaction",
    "TransactionType",
    "UnauthorizedError",
    "__version__",
    "coupons",
    "customers",
    "event_subscriptions",
    "products",
    "students",
    "subscriptions",
    "transactions",
    "utilities",
]
