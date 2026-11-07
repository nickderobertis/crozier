



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Budget,
        CardPaymentInstrument,
        Category,
        CreateAsyncFileUploadResponse,
        Department,
        ExpandableExpense,
        ExpandableExpenseBudget,
        ExpandableExpenseCategory,
        ExpandableExpenseDepartment,
        ExpandableExpenseLocation,
        ExpandableExpenseMerchant,
        ExpandableExpensePayment,
        ExpandableExpensePaymentStatus,
        ExpandableExpenseStatus,
        ExpandableExpenseUser,
        Expense,
        ExpenseCategory,
        ExpensePaymentStatus,
        ExpenseStatus,
        Location,
        Merchant,
        Money,
        OauthScope,
        PageExpandableExpense,
        Payment,
        PaymentInstrument,
        PaymentInstrument_Card,
        PaymentStatusReason,
        Receipt,
        User,
    )
    from .errors import BadRequestError, ForbiddenError, NotFoundError, UnauthorizedError
    from . import card_expenses
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "Budget": ".types",
    "CardPaymentInstrument": ".types",
    "Category": ".types",
    "CreateAsyncFileUploadResponse": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Department": ".types",
    "ExpandableExpense": ".types",
    "ExpandableExpenseBudget": ".types",
    "ExpandableExpenseCategory": ".types",
    "ExpandableExpenseDepartment": ".types",
    "ExpandableExpenseLocation": ".types",
    "ExpandableExpenseMerchant": ".types",
    "ExpandableExpensePayment": ".types",
    "ExpandableExpensePaymentStatus": ".types",
    "ExpandableExpenseStatus": ".types",
    "ExpandableExpenseUser": ".types",
    "Expense": ".types",
    "ExpenseCategory": ".types",
    "ExpensePaymentStatus": ".types",
    "ExpenseStatus": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "Location": ".types",
    "Merchant": ".types",
    "Money": ".types",
    "NotFoundError": ".errors",
    "OauthScope": ".types",
    "PageExpandableExpense": ".types",
    "Payment": ".types",
    "PaymentInstrument": ".types",
    "PaymentInstrument_Card": ".types",
    "PaymentStatusReason": ".types",
    "Receipt": ".types",
    "UnauthorizedError": ".errors",
    "User": ".types",
    "__version__": ".version",
    "card_expenses": ".card_expenses",
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
    "AsyncFernApi",
    "BadRequestError",
    "Budget",
    "CardPaymentInstrument",
    "Category",
    "CreateAsyncFileUploadResponse",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Department",
    "ExpandableExpense",
    "ExpandableExpenseBudget",
    "ExpandableExpenseCategory",
    "ExpandableExpenseDepartment",
    "ExpandableExpenseLocation",
    "ExpandableExpenseMerchant",
    "ExpandableExpensePayment",
    "ExpandableExpensePaymentStatus",
    "ExpandableExpenseStatus",
    "ExpandableExpenseUser",
    "Expense",
    "ExpenseCategory",
    "ExpensePaymentStatus",
    "ExpenseStatus",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "Location",
    "Merchant",
    "Money",
    "NotFoundError",
    "OauthScope",
    "PageExpandableExpense",
    "Payment",
    "PaymentInstrument",
    "PaymentInstrument_Card",
    "PaymentStatusReason",
    "Receipt",
    "UnauthorizedError",
    "User",
    "__version__",
    "card_expenses",
]
