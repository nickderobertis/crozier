



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .budget import Budget
    from .card_payment_instrument import CardPaymentInstrument
    from .category import Category
    from .create_async_file_upload_response import CreateAsyncFileUploadResponse
    from .department import Department
    from .expandable_expense import ExpandableExpense
    from .expandable_expense_budget import ExpandableExpenseBudget
    from .expandable_expense_category import ExpandableExpenseCategory
    from .expandable_expense_department import ExpandableExpenseDepartment
    from .expandable_expense_location import ExpandableExpenseLocation
    from .expandable_expense_merchant import ExpandableExpenseMerchant
    from .expandable_expense_payment import ExpandableExpensePayment
    from .expandable_expense_payment_status import ExpandableExpensePaymentStatus
    from .expandable_expense_status import ExpandableExpenseStatus
    from .expandable_expense_user import ExpandableExpenseUser
    from .expense import Expense
    from .expense_category import ExpenseCategory
    from .expense_payment_status import ExpensePaymentStatus
    from .expense_status import ExpenseStatus
    from .location import Location
    from .merchant import Merchant
    from .money import Money
    from .oauth_scope import OauthScope
    from .page_expandable_expense import PageExpandableExpense
    from .payment import Payment
    from .payment_instrument import PaymentInstrument, PaymentInstrument_Card
    from .payment_status_reason import PaymentStatusReason
    from .receipt import Receipt
    from .user import User
_dynamic_imports: typing.Dict[str, str] = {
    "Budget": ".budget",
    "CardPaymentInstrument": ".card_payment_instrument",
    "Category": ".category",
    "CreateAsyncFileUploadResponse": ".create_async_file_upload_response",
    "Department": ".department",
    "ExpandableExpense": ".expandable_expense",
    "ExpandableExpenseBudget": ".expandable_expense_budget",
    "ExpandableExpenseCategory": ".expandable_expense_category",
    "ExpandableExpenseDepartment": ".expandable_expense_department",
    "ExpandableExpenseLocation": ".expandable_expense_location",
    "ExpandableExpenseMerchant": ".expandable_expense_merchant",
    "ExpandableExpensePayment": ".expandable_expense_payment",
    "ExpandableExpensePaymentStatus": ".expandable_expense_payment_status",
    "ExpandableExpenseStatus": ".expandable_expense_status",
    "ExpandableExpenseUser": ".expandable_expense_user",
    "Expense": ".expense",
    "ExpenseCategory": ".expense_category",
    "ExpensePaymentStatus": ".expense_payment_status",
    "ExpenseStatus": ".expense_status",
    "Location": ".location",
    "Merchant": ".merchant",
    "Money": ".money",
    "OauthScope": ".oauth_scope",
    "PageExpandableExpense": ".page_expandable_expense",
    "Payment": ".payment",
    "PaymentInstrument": ".payment_instrument",
    "PaymentInstrument_Card": ".payment_instrument",
    "PaymentStatusReason": ".payment_status_reason",
    "Receipt": ".receipt",
    "User": ".user",
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
    "Budget",
    "CardPaymentInstrument",
    "Category",
    "CreateAsyncFileUploadResponse",
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
    "Location",
    "Merchant",
    "Money",
    "OauthScope",
    "PageExpandableExpense",
    "Payment",
    "PaymentInstrument",
    "PaymentInstrument_Card",
    "PaymentStatusReason",
    "Receipt",
    "User",
]
