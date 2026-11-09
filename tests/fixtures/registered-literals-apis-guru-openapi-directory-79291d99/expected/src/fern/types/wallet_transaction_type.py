

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WalletTransactionType(enum.StrEnum):
    """
    The type of the transaction. The supported transaction types that are returned are:
    `BANK_TRANSFER:` a transaction which credits an e-wallet through an external bank transfer.

    `PAYOUT:` a transaction which debits an e-wallet by disbursing funds to a counterparty.

    `PIS_PAY_IN:` a payment which credits an e-wallet through Plaid's Payment Initiation Services (PIS) APIs. For more information see the [Payment Initiation endpoints](https://plaid.com/docs/api/products/payment-initiation/).

    `REFUND:` a transaction which debits an e-wallet by refunding a previously initiated payment made through Plaid's [PIS APIs](https://plaid.com/docs/api/products/payment-initiation/).

    `FUNDS_SWEEP`: an automated transaction which debits funds from an e-wallet to a designated client-owned account.
    """

    BANK_TRANSFER = "BANK_TRANSFER"
    PAYOUT = "PAYOUT"
    PIS_PAY_IN = "PIS_PAY_IN"
    REFUND = "REFUND"
    FUNDS_SWEEP = "FUNDS_SWEEP"

    def visit(
        self,
        bank_transfer: typing.Callable[[], T_Result],
        payout: typing.Callable[[], T_Result],
        pis_pay_in: typing.Callable[[], T_Result],
        refund: typing.Callable[[], T_Result],
        funds_sweep: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WalletTransactionType.BANK_TRANSFER:
            return bank_transfer()
        if self is WalletTransactionType.PAYOUT:
            return payout()
        if self is WalletTransactionType.PIS_PAY_IN:
            return pis_pay_in()
        if self is WalletTransactionType.REFUND:
            return refund()
        if self is WalletTransactionType.FUNDS_SWEEP:
            return funds_sweep()
