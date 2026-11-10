

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Products(enum.StrEnum):
    """
    A list of products that an institution can support. All Items must be initialized with at least one product. The Balance product is always available and does not need to be specified during initialization.
    """

    ASSETS = "assets"
    AUTH = "auth"
    BALANCE = "balance"
    IDENTITY = "identity"
    INVESTMENTS = "investments"
    LIABILITIES = "liabilities"
    PAYMENT_INITIATION = "payment_initiation"
    IDENTITY_VERIFICATION = "identity_verification"
    TRANSACTIONS = "transactions"
    CREDIT_DETAILS = "credit_details"
    INCOME = "income"
    INCOME_VERIFICATION = "income_verification"
    DEPOSIT_SWITCH = "deposit_switch"
    STANDING_ORDERS = "standing_orders"
    TRANSFER = "transfer"
    EMPLOYMENT = "employment"
    RECURRING_TRANSACTIONS = "recurring_transactions"
    SIGNAL = "signal"

    def visit(
        self,
        assets: typing.Callable[[], T_Result],
        auth: typing.Callable[[], T_Result],
        balance: typing.Callable[[], T_Result],
        identity: typing.Callable[[], T_Result],
        investments: typing.Callable[[], T_Result],
        liabilities: typing.Callable[[], T_Result],
        payment_initiation: typing.Callable[[], T_Result],
        identity_verification: typing.Callable[[], T_Result],
        transactions: typing.Callable[[], T_Result],
        credit_details: typing.Callable[[], T_Result],
        income: typing.Callable[[], T_Result],
        income_verification: typing.Callable[[], T_Result],
        deposit_switch: typing.Callable[[], T_Result],
        standing_orders: typing.Callable[[], T_Result],
        transfer: typing.Callable[[], T_Result],
        employment: typing.Callable[[], T_Result],
        recurring_transactions: typing.Callable[[], T_Result],
        signal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Products.ASSETS:
            return assets()
        if self is Products.AUTH:
            return auth()
        if self is Products.BALANCE:
            return balance()
        if self is Products.IDENTITY:
            return identity()
        if self is Products.INVESTMENTS:
            return investments()
        if self is Products.LIABILITIES:
            return liabilities()
        if self is Products.PAYMENT_INITIATION:
            return payment_initiation()
        if self is Products.IDENTITY_VERIFICATION:
            return identity_verification()
        if self is Products.TRANSACTIONS:
            return transactions()
        if self is Products.CREDIT_DETAILS:
            return credit_details()
        if self is Products.INCOME:
            return income()
        if self is Products.INCOME_VERIFICATION:
            return income_verification()
        if self is Products.DEPOSIT_SWITCH:
            return deposit_switch()
        if self is Products.STANDING_ORDERS:
            return standing_orders()
        if self is Products.TRANSFER:
            return transfer()
        if self is Products.EMPLOYMENT:
            return employment()
        if self is Products.RECURRING_TRANSACTIONS:
            return recurring_transactions()
        if self is Products.SIGNAL:
            return signal()
