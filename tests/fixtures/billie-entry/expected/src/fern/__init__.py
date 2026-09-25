



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Amount,
        Debtor,
        DebtorAddress,
        DebtorPerson,
        ErrorResponse,
        Invoice,
        LineItem,
        Order,
        TokenResponse,
    )
    from .errors import BadRequestError, NotFoundError, UnauthorizedError
    from . import authentication, checkout, credit_notes, invoices, orders, reference_data
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "Amount": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "Debtor": ".types",
    "DebtorAddress": ".types",
    "DebtorPerson": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "ErrorResponse": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "Invoice": ".types",
    "LineItem": ".types",
    "NotFoundError": ".errors",
    "Order": ".types",
    "TokenResponse": ".types",
    "UnauthorizedError": ".errors",
    "__version__": ".version",
    "authentication": ".authentication",
    "checkout": ".checkout",
    "credit_notes": ".credit_notes",
    "invoices": ".invoices",
    "orders": ".orders",
    "reference_data": ".reference_data",
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
    "Amount",
    "AsyncFernApi",
    "BadRequestError",
    "Debtor",
    "DebtorAddress",
    "DebtorPerson",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "ErrorResponse",
    "FernApi",
    "FernApiEnvironment",
    "Invoice",
    "LineItem",
    "NotFoundError",
    "Order",
    "TokenResponse",
    "UnauthorizedError",
    "__version__",
    "authentication",
    "checkout",
    "credit_notes",
    "invoices",
    "orders",
    "reference_data",
]
