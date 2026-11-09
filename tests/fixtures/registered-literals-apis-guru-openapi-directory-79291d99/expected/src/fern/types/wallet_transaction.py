

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .wallet_transaction_amount import WalletTransactionAmount
from .wallet_transaction_counterparty import WalletTransactionCounterparty
from .wallet_transaction_status import WalletTransactionStatus
from .wallet_transaction_type import WalletTransactionType


class WalletTransaction(UniversalBaseModel):
    """
    The transaction details
    """

    amount: WalletTransactionAmount
    counterparty: WalletTransactionCounterparty
    created_at: dt.datetime = pydantic.Field()
    """
    Timestamp when the transaction was created, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format.
    """

    last_status_update: dt.datetime = pydantic.Field()
    """
    The date and time of the last time the `status` was updated, in IS0 8601 format
    """

    payment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The payment id that this transaction is associated with, if any. This is present only for transaction types `PIS_PAY_IN` and `REFUND`.
    """

    reference: str = pydantic.Field()
    """
    A reference for the transaction
    """

    status: WalletTransactionStatus
    transaction_id: str = pydantic.Field()
    """
    A unique ID identifying the transaction
    """

    type: WalletTransactionType = pydantic.Field()
    """
    The type of the transaction. The supported transaction types that are returned are:
    `BANK_TRANSFER:` a transaction which credits an e-wallet through an external bank transfer.
    
    `PAYOUT:` a transaction which debits an e-wallet by disbursing funds to a counterparty.
    
    `PIS_PAY_IN:` a payment which credits an e-wallet through Plaid's Payment Initiation Services (PIS) APIs. For more information see the [Payment Initiation endpoints](https://plaid.com/docs/api/products/payment-initiation/).
    
    `REFUND:` a transaction which debits an e-wallet by refunding a previously initiated payment made through Plaid's [PIS APIs](https://plaid.com/docs/api/products/payment-initiation/).
    
    `FUNDS_SWEEP`: an automated transaction which debits funds from an e-wallet to a designated client-owned account.
    """

    wallet_id: str = pydantic.Field()
    """
    The EMI (E-Money Institution) wallet that this payment is associated with, if any. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
