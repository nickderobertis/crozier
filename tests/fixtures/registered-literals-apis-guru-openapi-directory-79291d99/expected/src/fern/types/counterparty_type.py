

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CounterpartyType(enum.StrEnum):
    """
    The counterparty type.

    `merchant`: a provider of goods or services for purchase
    `financial_institution`: a financial entity (bank, credit union, BNPL, fintech)
    `payment_app`: a transfer or P2P app (e.g. Zelle)
    `marketplace`: a marketplace (e.g DoorDash, Google Play Store)
    `payment_terminal`: a point-of-sale payment terminal (e.g Square, Toast)
    """

    MERCHANT = "merchant"
    FINANCIAL_INSTITUTION = "financial_institution"
    PAYMENT_APP = "payment_app"
    MARKETPLACE = "marketplace"
    PAYMENT_TERMINAL = "payment_terminal"

    def visit(
        self,
        merchant: typing.Callable[[], T_Result],
        financial_institution: typing.Callable[[], T_Result],
        payment_app: typing.Callable[[], T_Result],
        marketplace: typing.Callable[[], T_Result],
        payment_terminal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CounterpartyType.MERCHANT:
            return merchant()
        if self is CounterpartyType.FINANCIAL_INSTITUTION:
            return financial_institution()
        if self is CounterpartyType.PAYMENT_APP:
            return payment_app()
        if self is CounterpartyType.MARKETPLACE:
            return marketplace()
        if self is CounterpartyType.PAYMENT_TERMINAL:
            return payment_terminal()
