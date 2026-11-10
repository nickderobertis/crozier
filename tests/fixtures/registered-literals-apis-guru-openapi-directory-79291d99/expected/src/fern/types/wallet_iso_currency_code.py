

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WalletIsoCurrencyCode(enum.StrEnum):
    """
    An ISO-4217 currency code, used with e-wallets and transactions.
    """

    GBP = "GBP"
    EUR = "EUR"

    def visit(self, gbp: typing.Callable[[], T_Result], eur: typing.Callable[[], T_Result]) -> T_Result:
        if self is WalletIsoCurrencyCode.GBP:
            return gbp()
        if self is WalletIsoCurrencyCode.EUR:
            return eur()
