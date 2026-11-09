

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreditAccountSubtype(enum.StrEnum):
    """
    Valid account subtypes for credit accounts. For a list containing descriptions of each subtype, see [Account schemas](https://plaid.com/docs/api/accounts/#StandaloneAccountType-credit).
    """

    CREDIT_CARD = "credit card"
    PAYPAL = "paypal"
    ALL = "all"

    def visit(
        self,
        credit_card: typing.Callable[[], T_Result],
        paypal: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreditAccountSubtype.CREDIT_CARD:
            return credit_card()
        if self is CreditAccountSubtype.PAYPAL:
            return paypal()
        if self is CreditAccountSubtype.ALL:
            return all_()
